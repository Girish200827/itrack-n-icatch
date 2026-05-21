import cv2
import numpy as np
import time as t
import pandas as pd

cap = cv2.VideoCapture(1)

start_time = t.perf_counter()
last_log_time = start_time

frame_count = 0
fps_data = []

while cap.isOpened():
    frame_start = t.perf_counter()

    ret, frame = cap.read()

    gray = frame
    gray = cv2.resize(gray, (500, 300))

    frame_end = t.perf_counter()
    frame_process_time = frame_end - frame_start
    instant_fps = 1 / (frame_process_time)

    frame_count += 1

    if frame_end - last_log_time >= 1.0:
        elasped = frame_end - start_time
        avg_fps = frame_count / (frame_end - last_log_time)
        avg_frame_time_ms = (frame_end - last_log_time) / frame_count * 1000, 2

        fps_data.append(
            {
                "time_sec": int(elasped),
                "avg_FPS": round(avg_fps, 2),
                "avg_frame_time_ms": round(frame_process_time * 1000, 2),
                "frame_count": frame_count,
                "last_log_time": last_log_time,
                "frame_end": frame_end,
            }
        )

        frame_count = 0
        last_log_time = frame_end

    cv2.putText(
        frame,
        f"FPS: {int(instant_fps)}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    cv2.imshow("frame", gray)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

df = pd.DataFrame(fps_data)
print(df)
