"""
This program has different options
to try with your camera such as:
- object tracking
- fps testing
- configuring camera settings
  for different cameras
"""

import logging_config
import logging

logging.basicConfig(filename="myapp")

# programs
from track_ping_pong_ball import TrackingPingPongBall

class TrackingObject:
    def __init__(self):
        self.track = TrackingPingPongBall()
        
        logging.warning('Finished')


good = TrackingObject()