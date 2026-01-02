"""
videocapture index:
0 --> droidcam video
1 --> hp laptop webcam
"""



import cv2
import numpy as np
import time as t
import pandas as pd


# record the start time when program begins
start_time = t.perf_counter()

# variable that will add to store fps 
add = 1



# creating the videocapture object 
# and reading from the input file

cap = cv2.VideoCapture(1)

# if cannot open the videocapture object then exit
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
 
# time when we processed last frame    
prev_frame_time = 0

# time at which we processed current frame
new_frame_time = 0

# Create a DataFrame
# so we can analyze the frame rate
fps_data = [{"time": 0, "FPS": 0}]

  
while True:
    # Caputure frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    gray = frame
    
    # resizing the frame size
    gray = cv2.resize(gray, (500, 300))
    
    # font to be used for displaying FPS
    font = cv2.FONT_HERSHEY_SIMPLEX
    # time when finish processing for this frame
    new_frame_time = t.time()
    
    # Calculating the fps
    
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    
    # converting the fps into integer
    fps = int(fps)
    
    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)
    
    # Storing fps
    
    # after every 5 seconds store the fps into the DataFrame 
    # so that we can see analyze it
    
    # calculate elasped time in seconds
    elasped_sec = t.perf_counter() - start_time
    
    # convert it to int so we can drop the decimals
    elasped_sec = int(elasped_sec)
    
    # after every 5 seconds print
    value = elasped_sec % (5 * add)
    if value == 0:
        
        # append the data into the list
        fps_data.append({"time": elasped_sec, "FPS": fps})
        
        # add one to this var
        add += 1
    
    # putting the FPS count on the frame
    cv2.putText(gray, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
    
    # display the video
    cv2.imshow('frame', gray)
    
    # press 'Q' if want to exit
    if cv2.waitKey(1) == ord('q'):
        
        # Create a dataframe from list of dicts
        df = pd.DataFrame(fps_data)
        
        print(df)
        
        # exit the program
        break

# When everything done, release the capture        
cap.release()
# Destroy the all windows now
cv2.destroyAllWindows()