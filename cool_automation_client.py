from pprint import pprint
from typing import Dict, List
from dictionaries import DictTypes, create_types_class
from swagger_client.api.services_api import ServicesApi
from swagger_client.api.units_api import UnitsApi
from swagger_client.models.types_response import TypesResponse
from swagger_client.models.types_response_data import TypesResponseData
from swagger_client.models.unit_response_data import UnitResponseData
from swagger_client.models.units_response import UnitsResponse
from swagger_client.rest import ApiException
from swagger_client.api.authentication_api import AuthenticationApi
from unit import HVACUnit


class CoolAutomationClient:
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
        self.unit_types = DictTypes(self._dictionaries["unitTypes"])
        self.brands = DictTypes(self._dictionaries.to_dict()["hvacBrands"])

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
        services_types = api.services_types_get(self.token, async_req=False)
        # services_types: TypesResponse = thread.get() 
        return services_types.data

    def get_controllable_units(self):
        """
        Retrieves the controllable units from the web api
        """
        # pp = pprint.PrettyPrinter(indent=4).pprint
        hvac_units: List[HVACUnit] = []
        api = UnitsApi()
        thread = api.units_get(self.token, 0, async_req=True)
        units: UnitsResponse = thread.get()        
        for _, unit in units.data.items():                        
            hvac_unit = HVACUnit(
                unit["id"], 
                unit["name"], 
                active_fan_mode=self.fan_modes[unit["activeFanMode"]],
                active_operation_mode=self.operation_modes[unit["activeOperationMode"]],
                active_operation_status=self.operation_statuses[unit["activeOperationStatus"]],
                active_setpoint=unit["activeSetpoint"],
                active_swing_mode=self.swing_modes[unit["activeSwingMode"]],
                ambient_temperature=unit["ambientTemperature"],                
                )
                                


api = CoolAutomationClient()
# dictionaries = api.get_dictionary()
# fan_modes = create_types_class(dictionaries.fan_modes)
# pprint(fan_modes.get_inverse('LOW'))
api.get_controllable_units()
