from typing import List

from cool_automation_client import CoolAutomationClient


class HVACUnit:
    def __init__(
        self,
        id: str,
        name: str,
        active_setpoint: int,
        active_operation_status: int,
        active_operation_mode: int,
        ambient_temperature: float,
        active_fan_mode: int,
        active_swing_mode: int,
        temerature_range: List[int],
        supported_operation_statuses: List[str],
        supported_operation_modes: List[str],
        supported_fan_modes: List[str],
        supported_swing_modes: List[str],
        client: CoolAutomationClient,
    ) -> None:
        self._id = id
        self._supported_operation_modes: List[str] = None
        self.supported_fan_modes: List[str] = None
        self.supported_swing_modes: List[str] = None
        self._change_filter_status: bool = False
        self._active_setpoint: int = active_setpoint
        self._ambient_temperature = ambient_temperature
        self._active_operation_status: int = active_operation_status
        self._active_operation_mode: int = active_operation_mode
        self._active_fan_mode: int = active_fan_mode
        self._active_swing_mode: int = active_swing_mode
        self._name: str = name
        self._temperature_range = temerature_range
        self._supported_operation_statuses = supported_operation_statuses
        self._supported_operation_modes = supported_operation_modes
        self._supported_fan_modes = supported_fan_modes
        self._supported_swing_modes = supported_swing_modes
        self._client = client

    def set_operation_status(self, status):
        self._client.set_operation_status(unit_id=self._id, status=status)

    def set_opration_mode(self, mode):
        self._client.set_operation_mode(unit_id=self._id, mode=mode)

    def set_swing_mode(self, mode):
        self._client.set_swing_mode(unit_id=self._id, mode=mode)

    def set_temperature_set_point(self, setpoint):
        self._client.set_temperature_set_point(unit_id=self._id, temp=setpoint)

    def __str__(self):
        return "%s(%s)" % (type(self).__name__, ", ".join("%s=%s" % item for item in vars(self).items()))
