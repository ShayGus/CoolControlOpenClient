import multiprocessing
from pprint import pprint

from swagger_client import UnitControlApi, UnitControlSwitchesBody
from swagger_client.api.services_api import ServicesApi
from swagger_client.api.units_api import UnitsApi
from swagger_client.models.types_response_data import TypesResponseData
from swagger_client.models.units_response import UnitsResponse
from swagger_client.rest import ApiException
from swagger_client.api.authentication_api import AuthenticationApi
from client.swagger_client.models.types_response import TypesResponse
from client.swagger_client.models.unit_control_modes_body import UnitControlModesBody
from client.swagger_client.models.unit_control_setpoints_body import UnitControlSetpointsBody
from client.swagger_client.models.unit_control_swings_body import UnitControlSwingsBody

from dictionaries import DictTypes
from utils.singleton import Singleton


class CoolAutomationClient(Singleton):
    """
    The client for CoolAutomationCloud service
    token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYxZjhkYmFlYThhMzFjMTk2NmIxZWNlYyIsImlhdCI6MTY0OTc2MDQxNiwiZXhwIjoxNjgxMzE4MDE2fQ.RLwz3qiZgLBRwHYpPQGrYtPC3t34axQBh2C7pP_wdVU
    """

    UNAUTHORIZES_ERROR_CODE = 401

    def __init__(
        self,
        token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYxZjhkYmFlYThhMzFjMTk2NmIxZWNlYyIsImlhdCI6MTY0OTc2MDQxNiwiZXhwIjoxNjgxMzE4MDE2fQ.RLwz3qiZgLBRwHYpPQGrYtPC3t34axQBh2C7pP_wdVU",
        username=None,
        password=None,
    ):
        self.token = token if not username else self.authenticate(username=username, password=password)
        self._dictionaries: TypesResponseData = self.get_dictionary()
        self.temperature_scale = DictTypes(self._dictionaries.temperature_scale)
        self.operation_statuses = DictTypes(self._dictionaries.operation_statuses)
        self.operation_modes = DictTypes(self._dictionaries.operation_modes)
        self.fan_modes = DictTypes(self._dictionaries.fan_modes)
        self.swing_modes = DictTypes(self._dictionaries.swing_modes)
        # self.device_types = DictTypes(self._dictionaries.device_types)
        # self.brands = DictTypes(self._dictionaries.hvac_brands)

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
        api_instance = UnitControlApi()
        body = UnitControlSetpointsBody(temp)

        try:
            # set unit operation status
            api_response = api_instance.units_unit_id_controls_setpoint_put(
                x_access_token=self.token, body=body, unit_id=unit_id
            )
        except ApiException as api_exception:
            print(f"Exception when calling UnitControlApi->units_unit_id_controls_switches_put: {api_exception}\n")


# api = CoolAutomationClient()
# dictionaries = api.get_dictionary()
# fan_modes = create_types_class(dictionaries.fan_modes)
# # pprint(fan_modes.get_inverse('LOW'))
# units = api.get_controllable_units()
# pprint(units)
