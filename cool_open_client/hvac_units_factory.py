import rel
from typing import List

from cool_open_client.cool_automation_client import CoolAutomationClient
from cool_open_client.unit import HVACUnit


class HVACUnitsFactory:
    def __init__(self) -> None:
        self._client = CoolAutomationClient()

    def generate_units_from_api(self) -> List[HVACUnit]:
        units = self._client.get_controllable_units()
        hvac_units: List[HVACUnit] = []
        for id, unit in units.data.items():
            if unit["type"] == 1:
                hvac_unit = HVACUnit(
                    id,
                    unit["name"],
                    active_fan_mode=self._client.fan_modes.get(unit["activeFanMode"]),
                    active_operation_mode=self._client.operation_modes.get(unit["activeOperationMode"]),
                    active_operation_status=self._client.operation_statuses.get(unit["activeOperationStatus"]),
                    active_setpoint=unit["activeSetpoint"],
                    active_swing_mode=self._client.swing_modes.get(unit["activeSwingMode"]),
                    ambient_temperature=unit["ambientTemperature"],
                    temerature_range=unit["temperatureLimits"]["0"],
                    supported_fan_modes=[self._client.fan_modes.get(mode) for mode in unit["supportedFanModes"]],
                    supported_operation_modes=[
                        self._client.operation_modes.get(mode) for mode in unit["supportedOperationModes"]
                    ],
                    supported_operation_statuses=[
                        self._client.operation_statuses.get(status) for status in unit["supportedOperationStatuses"]
                    ],
                    supported_swing_modes=[self._client.swing_modes.get(mode) for mode in unit["supportedSwingModes"]],
                    client=self._client,
                )
                hvac_units.append(hvac_unit)
        return hvac_units


factory = HVACUnitsFactory()
units = factory.generate_units_from_api()
factory._client.open_socket()
rel.signal(2, rel.abort)  # Keyboard Interrupt
rel.dispatch()
# units[0].set_operation_status('off')
