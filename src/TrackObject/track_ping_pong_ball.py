"""

Track a ping-pong ball using multi-threading
for video capturing and tracking to reduce latency.

"""

# setup logger for log messages
import logging
logger = logging.getLogger(__name__)


class TrackingPingPongBall:
    def __init__(self):
        self.run()
    
    def run(self):
        logger.info('Tracking the Ping Pong Ball with the following configurations: color config ...')