"""Module for updating nodes via frames."""
from .frames import (
    FrameGetAllNodesInformationNotification,
    FrameNodeStatePositionChangedNotification,
    FrameCommandRunStatusNotification)
from .opening_device import OpeningDevice, Blind
from .lightening_device import LighteningDevice
from .parameter import Intensity, Position, Parameter
from .pyvlx import PYVLXLOG


class NodeUpdater():
    """Class for updating nodes via incoming frames,  usually received by house monitor."""

    def __init__(self, pyvlx):
        """Initialize NodeUpdater object."""
        self.pyvlx = pyvlx

    async def process_frame(self, frame):
        """Update nodes via frame, usually received by house monitor."""
        if isinstance(frame, FrameNodeStatePositionChangedNotification) or \
                isinstance(frame, FrameGetAllNodesInformationNotification):
            if frame.node_id not in self.pyvlx.nodes:
                return
            node = self.pyvlx.nodes[frame.node_id]
            position = Position(frame.current_position)
            orientation = Position(frame.current_position_fp3)
            if isinstance(node, Blind):
                if position.position <= Parameter.MAX:
                    node.position = position
                    PYVLXLOG.debug("%s position changed to: %s" %(node.name, position))
                if orientation.position <= Parameter.MAX:
                    node.orientation = orientation
                    PYVLXLOG.debug("%s orientation changed to: %s" %(node.name, orientation))
                await node.after_update()
            elif isinstance(node, OpeningDevice):
                if position.position <= Parameter.MAX:
                    node.position = position
                await node.after_update()
            elif isinstance(node, LighteningDevice):
                intensity = Intensity(frame.current_position)
                if intensity.intensity <= Parameter.MAX:
                    node.intensity = intensity
                await node.after_update()