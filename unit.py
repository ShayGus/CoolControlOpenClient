from typing import List


class HVACUnit:

    def __init__(self, id: str, name: str, active_setpoint: int, 
                active_operation_status: int, active_operation_mode: int, 
                ambient_temperature: float, active_fan_mode: int, active_swing_mode: int) -> None:
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



    def _init_dictionaries(self):
        pass
