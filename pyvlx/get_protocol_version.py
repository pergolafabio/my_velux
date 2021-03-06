"""Module for retrieving protocol version from API."""
from .api_event import ApiEvent
from .frames import (
    FrameGetProtocolVersionConfirmation, FrameGetProtocolVersionRequest)


class GetProtocolVersion(ApiEvent):
    """Class for retrieving protocol version from API."""

    def __init__(self, pyvlx):
        """Initialize login class."""
        super().__init__(pyvlx=pyvlx)
        self.success = False
        self.version = None

    async def handle_frame(self, frame):
        """Handle incoming API frame, return True if this was the expected frame."""
        if not isinstance(frame, FrameGetProtocolVersionConfirmation):
            return False
        self.version = frame.version
        self.success = True
        return True

    def request_frame(self):
        """Construct initiating frame."""
        return FrameGetProtocolVersionRequest()
