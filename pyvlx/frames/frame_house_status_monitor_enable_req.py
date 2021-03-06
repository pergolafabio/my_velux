"""Module for requesting enabling the house status monitor."""
from ..const import Command

from .frame import FrameBase


class FrameHouseStatusMonitorEnableRequest(FrameBase):
    """Frame for requesting enabling the house status monitor."""

    PAYLOAD_LEN = 0

    def __init__(self):
        """Init Frame."""
        super().__init__(Command.GW_HOUSE_STATUS_MONITOR_ENABLE_REQ)
