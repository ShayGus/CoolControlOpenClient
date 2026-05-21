"""Public event types yielded by `CoolAutomationClient.subscribe_unit_updates`."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    # Imported only for type checkers — runtime import would create a
    # circular dependency with cool_automation_client.
    from .cool_automation_client import UnitUpdateMessage


@dataclass(frozen=True)
class UnitUpdate:
    """A real-time state change for a single HVAC unit.

    Carries the same `UnitUpdateMessage` shape produced by the HTTP path's
    `get_updated_controllable_unit` and `get_updated_controllable_units`,
    so consumers can feed it directly into `HVACUnit._update_unit`.
    """

    message: "UnitUpdateMessage"


@dataclass(frozen=True)
class Reconnected:
    """The WS connection dropped and was restored.

    Consumers should reconcile state — one or more `UnitUpdate` messages
    may have been missed during the gap.
    """

    pass


WsEvent = Union[UnitUpdate, Reconnected]
