from typing import List

from cool_open_client.utils.updatable import Updatable
from cool_open_client.cool_automation_client import CoolAutomationClient, UnitUpdateMessage


class HVACUnit(Updatable):
    """The logical clas repressentation of the HVAC unit"""

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
        self._client.register_for_updates(self)

    async def set_operation_status(self, status: str):
        """Set the operation status of the HVAC unit

        Args:
            status (str): String representation of the operation status
        """
        await self._client.set_operation_status(unit_id=self._id, status=status)

    async def set_opration_mode(self, mode: str):
        """Set the operation mode of the HVAC unit

        Args:
            mode (str): String representation of the operation mode
        """
        await self._client.set_operation_mode(unit_id=self._id, mode=mode)

    async def set_swing_mode(self, mode: str):
        """Set the swing mode of the HVAC unit

        Args:
            mode (str): String representation of the swing mode
        """
        await self._client.set_swing_mode(unit_id=self._id, mode=mode)

    async def set_temperature_set_point(self, setpoint: int):
        """Set the set point temperature of the HVAC unit

        Args:
            setpoint (int): The desired setpoint of the HVAC unit
        """
        await self._client.set_temperature_set_point(unit_id=self._id, temp=setpoint)

    def notify(self, message: UnitUpdateMessage):
        self._update_unit(message)

    def _update_unit(self, message: UnitUpdateMessage):
        self._active_operation_mode = message.operation_mode
        self._active_fan_mode = message.fan_mode
        self._active_operation_status = message.operation_status
        self._active_setpoint = message.setpoint
        self._active_swing_mode = message.swing

    @property
    def operation_mode(self):
        return self._active_operation_mode

    @property
    def fan_mode(self):
        return self._active_fan_mode

    @property
    def operation_status(self):
        return self._active_operation_status

    @property
    def setpoint(self):
        return self._active_setpoint

    @property
    def sing_mode(self):
        return self._active_swing_mode

    def get_updatable_id(self):
        return self._id

    def __str__(self):
        return "%s(%s)" % (type(self).__name__, ", ".join("%s=%s" % item for item in vars(self).items()))
