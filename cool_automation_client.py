from pprint import pprint
from typing import Dict
from dictionaries import create_types_class
from swagger_client.api.services_api import ServicesApi
from swagger_client.api.units_api import UnitsApi
from swagger_client.models.types_response import TypesResponse
from swagger_client.rest import ApiException
from swagger_client.api.authentication_api import AuthenticationApi


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

    def get_dictionary(self) -> Dict:
        api = ServicesApi()
        thread = api.services_types_get(self.token, async_req=True)
        services_types: TypesResponse = thread.get()    
        return services_types.data

    def get_controllable_units(self):
        """
        Retrieves the controllable units from the web api
        """
        # pp = pprint.PrettyPrinter(indent=4).pprint

        api = UnitsApi()
        thread = api.units_get(self.token, 0, async_req=True)
        units = thread.get()
        pprint(units.data)
        # api = DeviceApi()
        # for _, data in units.data.items():
        #     for unit in data["units"]:
        #         thread = api.devices_device_id_get(self.token, unit, async_req=True)
        #         u = thread.get()
        #         pprint(u)


api = CoolAutomationClient()
dictionaries = api.get_dictionary()
fan_modes = create_types_class(dictionaries.fan_modes)
pprint(fan_modes.get_inverse('LOW'))
