from pprint import pprint
from typing import Dict, Union
import marshmallow
import marshmallow_dataclass
import websocket
import rel
import json
from dataclasses import dataclass, field

from cool_open_client.client import UnitControlApi, UnitControlSwitchesBody
from cool_open_client.client.api.services_api import ServicesApi
from cool_open_client.client.api.units_api import UnitsApi
from cool_open_client.client.models.types_response_data import TypesResponseData
from cool_open_client.client.models.units_response import UnitsResponse
from cool_open_client.client.rest import ApiException
from cool_open_client.client.api.authentication_api import AuthenticationApi
from cool_open_client.client.models.types_response import TypesResponse
from cool_open_client.client.models.unit_control_modes_body import UnitControlModesBody
from cool_open_client.client.models.unit_control_setpoints_body import UnitControlSetpointsBody
from cool_open_client.client.models.unit_control_swings_body import UnitControlSwingsBody

from cool_open_client.utils.dictionaries import DictTypes
from cool_open_client.utils.singleton import Singleton
from cool_open_client.utils.updatable import Updatable

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
    temperature_scale: int = field(metadata={"required": True, "data_key": "temperatureScale"})


UnitUpdateMessageSchema = marshmallow_dataclass.class_schema(UnitUpdateMessage)


class CoolAutomationClient(Singleton):
    """
    The coolautomation_client for CoolAutomationCloud service    
    """

    UNAUTHORIZES_ERROR_CODE = 401
    SOCKET_URI = "wss://api.coolremote.net/api/v1/"

    def __init__(
        self,
        token=None,
        username=None,
        password=None,
    ):
        if token is None and username is None and password is None:
            raise ValueError("Toke or Username and Password must be provided")
        self.token = token if not username else self.authenticate(username=username, password=password)
        self._dictionaries: TypesResponseData = self.get_dictionary()
        self.temperature_scale = DictTypes(self._dictionaries.temperature_scale)
        self.operation_statuses = DictTypes(self._dictionaries.operation_statuses)
        self.operation_modes = DictTypes(self._dictionaries.operation_modes)
        self.fan_modes = DictTypes(self._dictionaries.fan_modes)
        self.swing_modes = DictTypes(self._dictionaries.swing_modes)
        # self.device_types = DictTypes(self._dictionaries.device_types)
        # self.brands = DictTypes(self._dictionaries.hvac_brands)
        self.socket = None
        self._registered_units: Dict[str, Updatable] = {}

    @classmethod
    def authenticate(cls, username: str, password: str) -> str:
        """
        Perform Authentication
        """
        body = {"username": username, "password": password}
        api = AuthenticationApi()
        try:
            thread = api.authenticate_post(body, async_req=True)
            result = thread.get()
        except ApiException as error:
            if error.status == cls.UNAUTHORIZES_ERROR_CODE:
                return "Unauthorized"
        return result.data["token"]

    def get_dictionary(self) -> TypesResponseData:
        """
        Pulls dictionary from the API

        Returns:
            TypesResponseData: Dictionary from api service
        """
        api = ServicesApi()
        thread = api.services_types_get(self.token, async_req=True)
        service_types: TypesResponse = thread.get()
        return service_types.data

    def get_controllable_units(self) -> UnitsResponse:
        """
        Retrieves the controllable units from the web api
        """
        # pp = pprint.PrettyPrinter(indent=4).pprint
        api = UnitsApi()
        thread = api.units_get(self.token, async_req=True)
        units: UnitsResponse = thread.get()
        return units

    def set_operation_status(self, unit_id: str, status: str):
        """
        Set the operation status of the device

        Args:
            unit_id (str): Unit ID
            status (str): Status
        """
        api_instance = UnitControlApi()
        status = self.operation_statuses.get_inverse(status)
        body = UnitControlSwitchesBody(status)

        try:
            # set unit operation status
            api_response = api_instance.units_unit_id_controls_switches_put(
                x_access_token=self.token, body=body, unit_id=unit_id
            )
        except ApiException as api_exception:
            print(f"Exception when calling UnitControlApi->units_unit_id_controls_switches_put: {api_exception}\n")

    def set_operation_mode(self, unit_id: str, mode: str):
        """
        Sets the operation mode of the HVAC unit

        Args:
            unit_id (str): The ID of the unit
            mode (str): The mode to set the unit to
        """
        api_instance = UnitControlApi()
        status = self.operation_modes.get_inverse(mode)
        body = UnitControlModesBody(status)

        try:
            # set unit operation status
            api_response = api_instance.units_unit_id_controls_modes_put(
                x_access_token=self.token, body=body, unit_id=unit_id
            )
        except ApiException as api_exception:
            print(f"Exception when calling UnitControlApi->units_unit_id_controls_switches_put: {api_exception}\n")

    def set_swing_mode(self, unit_id: str, mode: str):
        """Set the swing mode of the HVAC unit

        Args:
            unit_id (str): Unit ID
            mode (str): The swing mode to set on the device
        """
        api_instance = UnitControlApi()
        mode = self.swing_modes.get_inverse(mode)
        body = UnitControlSwingsBody(mode)

        try:
            # set unit operation status
            api_response = api_instance.units_unit_id_controls_swings_put(
                x_access_token=self.token, body=body, unit_id=unit_id
            )
        except ApiException as api_exception:
            print(f"Exception when calling UnitControlApi->units_unit_id_controls_switches_put: {api_exception}\n")

    def set_temperature_set_point(self, unit_id: str, temp: int):
        """Set the desired setpoint on the HVAC unit

        Args:
            unit_id (str): The identifier of the unit
            temp (int): The desired setpoint temperature
        """
        api_instance = UnitControlApi()
        body = UnitControlSetpointsBody(temp)

        try:
            # set unit operation status
            api_response = api_instance.units_unit_id_controls_setpoints_put(
                x_access_token=self.token, body=body, unit_id=unit_id
            )
        except ApiException as api_exception:
            print(f"Exception when calling UnitControlApi->units_unit_id_controls_switches_put: {api_exception}\n")

    def register_for_updates(self, unit: Updatable):
        """Register an HVAC unit to receive updates from service calls or WebSocket

        Args:
            unit (Updatable): The identifier of the unit
        """
        self._registered_units[unit.get_updatable_id()] = unit

    def on_open_socket(self, ws):
        pass

    def on_close_socket(self, ws, message):
        pass

    def on_message_socket(self, ws, message):
        """Handle message received from socket

        Args:
            ws (_type_): WebSocket instance
            message (_type_): Received message
        """
        loaded_json = json.loads(message)
        pprint(loaded_json)
        self._handle_ping_pong(ws, loaded_json)
        self._handle_ws_message(loaded_json)

    def _handle_ping_pong(self, ws, loaded_json):
        if loaded_json.get("type", None) == "ping":
            ws.send('{"type":"pong"}')

    def _handle_ws_message(self, loaded_json):
        data = loaded_json.get("data", None)
        if data is not None:
            pprint(data)
            update_message: UnitUpdateMessage = UnitUpdateMessageSchema().load(data, unknown=marshmallow.EXCLUDE)
            if update_message is not None:
                unit = self._registered_units.get(update_message.unit_id)
                update_message = self._transform_message(update_message)
                unit.notify(update_message)

    def on_error_socket(self, ws, message):
        print(message)

    def open_socket(self):
        """
        Open a websocket to the CoolAutomationsServer
        """
        try:
            # websocket.enableTrace(True)
            self.socket = websocket.WebSocketApp(
                self.SOCKET_URI,
                on_open=self.on_open_socket,
                on_message=self.on_message_socket,
                on_error=self.on_error_socket,
                on_close=self.on_close_socket,
            )

            self.socket.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
            self.socket.send(f'{{"type":"authenticate","content":{{"token":"{self.token}"}}}}')
        except Exception as socket_exception:
            print(f"Exception when calling UnitControlApi->units_unit_id_controls_switches_put: {socket_exception}\n")

    def _transform_message(self, message: UnitUpdateMessage) -> UnitUpdateMessage:
        message.fan_mode = self.fan_modes.get(message.fan_mode)
        message.swing = self.swing_modes.get(message.swing)
        message.operation_mode = self.operation_modes.get(message.operation_mode)
        message.operation_status = self.operation_statuses.get(message.operation_status)
        return message


# api = CoolAutomationClient()
# dictionaries = api.get_dictionary()
# fan_modes = create_types_class(dictionaries.fan_modes)
# # pprint(fan_modes.get_inverse('LOW'))
# units = api.get_controllable_units()
# pprint(units)
