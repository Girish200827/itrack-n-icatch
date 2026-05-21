"""
Test the logic used to calculate
the fps
"""


import time
import pandas as pd
import cv2
import sys
import keyboard

start_time = time.perf_counter()

add_var = 1

fps_data = [{"time": 0, "FPS": 0}]

def store_fps_data(start_time, mult_var):

    elasped_sec = int(time.perf_counter() - start_time)
    
    value = elasped_sec % (5 * mult_var)
    if value == 0:
        
        fps_data.append({"time": elasped_sec, "FPS": add_var})
        
        
        
while True:
    
    collect_fps = store_fps_data(start_time, mult_var=(1 + add_var))
    
    add_var += 1
    
    if keyboard.is_pressed('q'):
        
        #df = pd.DataFrame(fps_data)
        
        #print(df)
        
        sys.exit(0)
    