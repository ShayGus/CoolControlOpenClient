import functools
import logging
import threading
from time import sleep
import websocket
from typing import Dict, Iterable, List, Union, cast

import json
from dataclasses import dataclass, field
import marshmallow
import marshmallow_dataclass

# import websockets
from websocket import WebSocketConnectionClosedException
from .client.api_client import ApiClient

from cool_open_client.client.models.unit_control_fans_body import UnitControlFansBody
from cool_open_client.client.api.me_api import MeApi
from cool_open_client.client.models.user_response_data import UserResponseData


from cool_open_client.client.api.devices_api import DevicesApi
from cool_open_client.client.models.device_response_data import DeviceResponseData
from cool_open_client.client.models.devices_response import DevicesResponse
from cool_open_client.client.models.devices_response_data import DevicesResponseData

from cool_open_client.client import UnitControlApi, UnitControlSwitchesBody
from cool_open_client.client.api.services_api import ServicesApi
from cool_open_client.client.api.units_api import UnitsApi
from cool_open_client.client.api.unit_api import UnitApi
from cool_open_client.client.models.types_response_data import TypesResponseData
from cool_open_client.client.models.units_response import UnitsResponse
from cool_open_client.client.models.unit_response import UnitResponse
from cool_open_client.client.models.unit_response_data import UnitResponseData
from cool_open_client.client.rest import ApiException
from cool_open_client.client.api.authentication_api import AuthenticationApi
from cool_open_client.client.models.unit_control_modes_body import UnitControlModesBody
from cool_open_client.client.models.unit_control_setpoints_body import UnitControlSetpointsBody
from cool_open_client.client.models.unit_control_swings_body import UnitControlSwingsBody

from cool_open_client.utils.dictionaries import DictTypes
from cool_open_client.utils.singleton import Singleton
from cool_open_client.utils.updatable import Updatable
from cool_open_client.utils.dict_to_model import dict_to_model

import sys

_LOGGER = logging.getLogger(__package__)
_LOGGER.addHandler(logging.StreamHandler(sys.stdout))
_LOGGER.setLevel(logging.DEBUG)

###
# {'data': {'ambientTemperature': 29,
#           'deviceId': '61bb087a212f1c7c42b9e76a',
#           'fan': 3,
#           'filter': False,
#           'internalId': '283B960300D4:31303336',
#           'operationMode': 0,
#           'operationStatus': 2,
#           'serviceUnits': [],
#           'setpoint': 25,
#           'site': '61f8e091a8a31c1966b33a29',
#           'swing': 6,
#           'temperatureScale': 1,
#           'unitId': '61f8e56960bf483d1e5b0743'},
#  'name': 'UPDATE_UNIT'}
###


@dataclass
class UnitUpdateMessage:
    """Data class representing the update message received from the server"""

    ambient_temperature: int = field(metadata={"required": False, "data_key": "ambientTemperature"})
    unit_id: str = field(metadata={"required": True, "data_key": "unitId"})
    fan_mode: Union[str, int] = field(metadata={"required": True, "data_key": "fan"})
    filter: bool = field(metadata={"required": False, "data_key": "filter"})
    operation_mode: Union[str, int] = field(metadata={"required": True, "data_key": "operationMode"})
    operation_status: Union[str, int] = field(metadata={"required": True, "data_key": "operationStatus"})
    setpoint: int = field(metadata={"required": True, "data_key": "setpoint"})
    swing: Union[str, int] = field(metadata={"required": True, "data_key": "swing"})
    temperature_scale: int = field(metadata={"required": False, "data_key": "temperatureScale"}, default = 1)


UnitUpdateMessageSchema = marshmallow_dataclass.class_schema(UnitUpdateMessage)


def with_exception(function):
    @functools.wraps(function)
    async def wrapper(*args, **kwargs):
        try:
            return await function(*args, **kwargs)
        except ApiException as exception:
            body = json.loads(exception.body)
            if (
                exception.status == CoolAutomationClient.UNAUTHORIZES_ERROR_CODE
                and body["message"] == "Token verification failed"
            ):
                raise InvalidTokenException() from exception
            else:
                raise exception

    return wrapper


class CoolAutomationClient(Singleton):
    """
    The coolautomation_client for CoolAutomationCloud service
    """

    UNAUTHORIZES_ERROR_CODE = 401
    SOCKET_URI = "wss://api.coolremote.net/api/v1/"

    @classmethod
    async def create(cls, token, logger=None):
        self = cls(logger=logger)
        if token is None:
            raise ValueError("Toke cannot be None")
        self.token = token
        dictionaries = await self.get_dictionary()
        self._dictionaries: TypesResponseData = dictionaries
        self.temperature_scale = DictTypes(dictionaries.temperature_scale)
        self.operation_statuses = DictTypes(dictionaries.operation_statuses)
        self.operation_modes = DictTypes(dictionaries.operation_modes)
        self.fan_modes = DictTypes(dictionaries.fan_modes)
        self.swing_modes = DictTypes(dictionaries.swing_modes)
        return self

    @classmethod
    async def authenticate(cls, username: str, password: str) -> str:
        """
        Perform Authentication
        """
        body = {"username": username, "password": password}
        api = AuthenticationApi()
        try:
            result = await api.authenticate_post(body)
        except ApiException as error:
            if error.status == cls.UNAUTHORIZES_ERROR_CODE:
                return "Unauthorized"
        return result.data.token

    def __init__(self, logger: logging.Logger = None) -> None:
        self.token = None
        self._dictionaries: TypesResponseData = None
        self.temperature_scale = None
        self.operation_statuses = None
        self.operation_modes = None
        self.fan_modes = None
        self.swing_modes = None
        # self.device_types = DictTypes(self._dictionaries.device_types)
        # self.brands = DictTypes(self._dictionaries.hvac_brands)
        self.socket = None
        self._registered_units: Dict[str, Updatable] = {}
        self.api_client = ApiClient()
        self.logger = logger if logger is not None else _LOGGER

    @with_exception
    async def get_me(self) -> UserResponseData:
        api = MeApi(api_client=self.api_client)
        response = await api.me_get(self.token)
        return response.data

    @with_exception
    async def get_dictionary(self) -> TypesResponseData:
        """
        Pulls dictionary from the API

        Returns:
            TypesResponseData: Dictionary from api service
        """
        api = ServicesApi(self.api_client)
        response = await api.services_types_get(self.token)
        return response.data

    @with_exception
    async def get_controllable_units(self) -> UnitsResponse:
        """
        Retrieves the controllable units from the web api
        """
        # pp = pprint.PrettyPrinter(indent=4).pprint
        api = UnitsApi(api_client=self.api_client)
        units: UnitsResponse = await api.units_get(self.token)

        return units

    @with_exception
    async def get_updated_controllable_unit(self, unit_id: str) -> UnitUpdateMessage:
        """
        Retrieves the controllable units from the web api
        """
        api = UnitApi(api_client=self.api_client)
        unit: UnitResponseData = (await api.units_unit_id_get(self.token, unit_id)).data

        message = UnitUpdateMessage(
            ambient_temperature=unit.ambient_temperature,
            fan_mode=unit.active_fan_mode,
            operation_mode=unit.active_operation_mode,
            setpoint=unit.active_setpoint,
            swing=unit.active_swing_mode,
            operation_status=unit.active_operation_status,
            filter=unit.filter,
            unit_id=unit.id,
        )
        return self._transform_message(message)

    @with_exception
    async def get_devices(self) -> List[Union[DeviceResponseData, None]]:
        api = DevicesApi(api_client=self.api_client)
        devices: DevicesResponse = await api.devices_get(self.token)
        data: DevicesResponseData = devices.data
        devices = [
            dict_to_model(DeviceResponseData, device)
            for device in cast(Iterable[DeviceResponseData], data.values())
            if device["isConnected"]
        ]
        return devices

    @with_exception
    async def set_operation_status(self, unit_id: str, status: str):
        """
        Set the operation status of the device

        Args:
            unit_id (str): Unit ID
            status (str): Status
        """
        api_instance = UnitControlApi(api_client=self.api_client)
        status = self.operation_statuses.get_inverse(status)
        body = UnitControlSwitchesBody(status)

        # set unit operation status
        api_response = await api_instance.units_unit_id_controls_switches_put(
            x_access_token=self.token, body=body, unit_id=unit_id
        )

    @with_exception
    async def set_operation_mode(self, unit_id: str, mode: str):
        """
        Sets the operation mode of the HVAC unit

        Args:
            unit_id (str): The ID of the unit
            mode (str): The mode to set the unit to
        """
        api_instance = UnitControlApi(api_client=self.api_client)
        status = self.operation_modes.get_inverse(mode)
        body = UnitControlModesBody(status)

        api_response = await api_instance.units_unit_id_controls_modes_put(
            x_access_token=self.token, body=body, unit_id=unit_id
        )

    @with_exception
    async def set_swing_mode(self, unit_id: str, mode: str):
        """Set the swing mode of the HVAC unit

        Args:
            unit_id (str): Unit ID
            mode (str): The swing mode to set on the device
        """
        api_instance = UnitControlApi(api_client=self.api_client)
        mode = self.swing_modes.get_inverse(mode)
        body = UnitControlSwingsBody(mode)

        api_response = await api_instance.units_unit_id_controls_swings_put(
            x_access_token=self.token, body=body, unit_id=unit_id
        )

    @with_exception
    async def set_fan_mode(self, unit_id: str, mode: str):
        """Set the fan mode of the HVAC unit

        Args:
            unit_id (str): Unit ID
            mode (str): The fan mode to set on the device
        """
        api_instance = UnitControlApi(api_client=self.api_client)
        mode = self.fan_modes.get_inverse(mode)
        body = UnitControlFansBody(mode)

        api_response = await api_instance.units_unit_id_controls_fans_put(
            x_access_token=self.token, body=body, unit_id=unit_id
        )

    @with_exception
    async def set_temperature_set_point(self, unit_id: str, temp: int):
        """Set the desired setpoint on the HVAC unit

        Args:
            unit_id (str): The identifier of the unit
            temp (int): The desired setpoint temperature
        """
        api_instance = UnitControlApi(self.api_client)
        body = UnitControlSetpointsBody(temp)

        api_response = await api_instance.units_unit_id_controls_setpoints_put(
            x_access_token=self.token, body=body, unit_id=unit_id
        )

    def register_for_updates(self, unit: Updatable):
        """Register an HVAC unit to receive updates from service calls or WebSocket

        Args:
            unit (Updatable): The identifier of the unit
        """
        self._registered_units[unit.get_updatable_id()] = unit

    def on_open_socket(self, ws):
        ws.send(f'{{"type":"authenticate","content":{{"token":"{self.token}"}}}}')

    def on_close_socket(self, ws, message: str):
        raise WebSocketConnectionClosedException()

    def on_message_socket(self, ws, message):
        """Handle message received from socket

        Args:
            ws (_type_): WebSocket instance
            message (_type_): Received message
        """
        try:
            loaded_json = json.loads(message)
            _LOGGER.debug(f"Message from socket: {message}")
            self._handle_ping_pong(ws, loaded_json)
            self._handle_ws_message(loaded_json)
        except Exception as error:
            self.logger.error(error)
            raise error

    def _handle_ping_pong(self, ws, loaded_json):
        self.logger.debug(f"Entered Ping Pong Handler %s" % loaded_json.get("type", "Not Ping Pong"))
        if loaded_json.get("type", None) == "ping":
            self.logger.debug("...Ping Pong...")
            ws.send('{"type":"pong"}')
        self.logger.debug("Exiting Ping Pong Handler")

    def _handle_ws_message(self, loaded_json):
        self.logger.debug("Entered Message Handler")
        data = loaded_json.get("data", None)
        if data is not None:
            self.logger.debug(f"Received data from websocket: %s" % str(data))
            update_message: UnitUpdateMessage = UnitUpdateMessageSchema().load(data, unknown=marshmallow.EXCLUDE)
            if update_message is not None:
                unit = self._registered_units.get(update_message.unit_id)
                update_message = self._transform_message(update_message)
                if unit is not None:
                    unit.notify(update_message)
        self.logger.debug("Exiting Message Handler")

    def on_error_socket(self, ws: websocket.WebSocketApp, message: str):
        self.logger.error(message)
        raise WebSocketConnectionClosedException()

    def open_socket(self):
        """
        Open a websocket to the CoolAutomationsServer
        """
        self.logger.debug("Entered open socket")
        try:
            # async with websockets.connect(self.SOCKET_URI) as websocket:
            #     self.logger.debug("Sent connection request to server")
            #     await websocket.send(f'{{"type":"authenticate","content":{{"token":"{self.token}"}}}}')
            #     response = await websocket.recv()
            #     loaded_json = json.loads(response)
            #     await self._handle_ping_pong(websocket, loaded_json)
            #     # self.logger.debug(f"Received auth auth done: {response}")
            #     await self._ws_handler(websocket)
            #     # await asyncio.sleep(0)

            # websocket.enableTrace(True)
            self.socket = websocket.WebSocketApp(
                self.SOCKET_URI,
                on_open=self.on_open_socket,
                on_message=self.on_message_socket,
                on_error=self.on_error_socket,
                on_close=self.on_close_socket,
            )
            ws_thread = threading.Thread(target=self.socket.run_forever)
            ws_thread.name = "CoolAutomationClientWebsocketClient"
            ws_thread.daemon = True
            ws_thread.start()

            # self.socket.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
            # task = ws.init(self.SOCKET_URI, self.on_message_socket)
            return ws_thread
        except Exception as socket_exception:
            self.logger.error(f"Exception when calling open socket: {socket_exception}\n")

    async def _ws_handler(self, websocket):
        self.logger.debug("Entered websocket handler")
        async for message in websocket:
            try:
                self.logger.debug(f"Data received from socket: %s" % message)
                loaded_json = json.loads(message)
                await self._handle_ping_pong(websocket, loaded_json)
                await self._handle_ws_message(loaded_json)
            except websockets.ConnectionClosedOK:
                self.logger.debug("Connection closed")
                break
            except Exception as error:
                self.logger.error("Unhandled error occured in _ws_handler method: %s", error)
                break

    def _transform_message(self, message: UnitUpdateMessage) -> UnitUpdateMessage:
        message.fan_mode = self.fan_modes.get(message.fan_mode)
        message.swing = self.swing_modes.get(message.swing)
        message.operation_mode = self.operation_modes.get(message.operation_mode)
        message.operation_status = self.operation_statuses.get(message.operation_status)
        return message


class UnauthorizedException(Exception):
    pass


class InvalidTokenException(Exception):
    pass


# async def t():
#     api = CoolAutomationClient
#     r = await api.authenticate(username="aa", password="aaa")
#     return r

# loop = asyncio.get_event_loop()
# res = loop.run_until_complete(asyncio.gather(t()))
# pprint(res)
# # dictionaries = api.get_dictionary()
# # fan_modes = create_types_class(dictionaries.fan_modes)
# # # pprint(fan_modes.get_inverse('LOW'))
# # units = api.get_controllable_units()
# # pprint(units)
