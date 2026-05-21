import cv2 as cv
import numpy as np
import time as t
import pandas as pd


face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)


cap = cv.VideoCapture(2)  # 2 for dashcam


# varibales that will be used to find fps
prev_frame_time = 0
new_frame_time = 0

# var that will be used to store fps into a list
add_val = 1
start_time = t.perf_counter()

# list for storing the fps
fps_data = [{"time": 0, "FPS": 0, "add_val": 1}]


# Function to store fps into a list
def store_fps_data(elasped_time, add_val):

    if elasped_time == add_val:

        fps_data.append(
            {"begin": start_time, "time": elasped_time, "FPS": fps, "add_val": add_val}
        )

        add_val += 1

    return add_val


def save(fps_data):
    df = pd.DataFrame(fps_data)

    return df


while cap.isOpened():
    ret, frame = cap.read()

    gray = frame

    gray = cv.resize(gray, (500, 300))

    scale_gray = cv.cvtColor(gray, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(scale_gray, scaleFactor=1.1, minNeighbors=5)

    # Display fps

    font = cv.FONT_HERSHEY_SIMPLEX
    new_frame_time = t.time()

    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    fps = int(fps)
    fps = str(fps)

    cv.putText(gray, fps, (7, 70), font, 3, (100, 255, 0), 3, cv.LINE_AA)

    # Storing FPS to a list through a function
    elasped_time = int(t.perf_counter() - start_time)
    add_val = store_fps_data(elasped_time, add_val)

    # Bounding a box around the face
    for x, y, w, h in faces:
        cv.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv.imshow("frame", gray)
    if cv.waitKey(1) == ord("p"):
        break

cap.release()
cv.destroyAllWindows()

# print(save(fps_data))  # print the data for the fps
