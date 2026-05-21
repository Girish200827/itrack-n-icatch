"""
This script is to optimize the performance of object detection algorithms
by using multi-threading for video capturing to reduce latency.
"""

import cv2
from queue import Queue
from threading import Thread


class VideoCapture:
    def __init__(self, index):
        self.index = index
        self.cap = cv2.VideoCapture(index)
        self.q = Queue()
        self.running = True

    def capture(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break
            self.q.put(frame)

    def get_frame(self):
        return self.q.get()

    def release(self):
        self.running = False
        self.cap.release()


# Usage
cap = VideoCapture(1)  # index 1 => laptop webcam

thread = Thread(target=cap.capture)
thread.start()

while True:
    frame = cap.get_frame()

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord("v"):
        break

cap.release()
cv2.destroyAllWindows()
