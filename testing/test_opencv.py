"""
This python script is for basic testing of video capturing (through opencv),
and calculating and displaying the FPS (frames per seconds) as a metrics to
assess the performance of this algorithm.

videocapture index:
0 --> droidcam video

if no external camera connected then:
1 --> hp dashcamera

if an external secondary camera connected then:
1 --> second camera
2 --> hp dashcamera
"""

import cv2
import numpy as np
import time as t
import pandas as pd


start_time = t.perf_counter()  # record the start time when program begins

add = 1  # variable that will add to store fps


# create the VideoCapture object
# and read it from the input file

cap = cv2.VideoCapture(1)  # index 1 for laptop camera

# if cannot open the VideoCapture object then exit
if not cap.isOpened():
    print("Cannot open camera")
    exit()


prev_frame_time = 0  # time when we processed last frame

new_frame_time = 0  # time at which we processed current frame

# Create a DataFrame
# so we can analyze the frame rate
fps_data = [{"time": 0, "FPS": 0, "Frame Rate": 0}]


while True:

    ret, frame = cap.read()  # Caputure frame-by-frame

    gray = frame  # Our operations on the frame come here

    gray = cv2.resize(gray, (500, 300))  # resizing the frame size

    font = cv2.FONT_HERSHEY_SIMPLEX  # font to be used for displaying FPS

    new_frame_time = t.time()  # time when finish processing for this frame

    # Calculating the fps

    # calculating processing time for each frame
    frame_process_time = new_frame_time - prev_frame_time

    fps = 1 / (frame_process_time)
    prev_frame_time = new_frame_time

    fps = int(fps)  # converting the fps into integer

    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)

    # Storing fps

    # after every 5 seconds store the fps into the DataFrame
    # so that we can see analyze it

    elasped_sec = t.perf_counter() - start_time  # calculate elasped time in seconds

    # convert it to int so we can drop the decimals
    elasped_sec = int(elasped_sec)

    value = elasped_sec % (5 * add)  # after every 5 seconds print
    if value == 0:

        # append the data into the list
        fps_data.append(
            {"time": elasped_sec, "FPS": fps, "Frame Rate": frame_process_time}
        )

        add += 1  # add one to this var

    # putting the FPS count on the frame
    cv2.putText(gray, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow("frame", gray)  # display the video

    # press 'Q' if want to exit
    if cv2.waitKey(1) == ord("q"):

        # Create a dataframe from list of dicts
        df = pd.DataFrame(fps_data)

        print(df)

        # exit the program
        break


cap.release()  # When everything done, release the capture
cv2.destroyAllWindows()  # Destroy the all windows now
