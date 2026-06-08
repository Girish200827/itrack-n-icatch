"""
This is one and only script for all the
Arduino CLI options needed for this project.

Options needed:
- Show devices Connected
- Edit/Update/Compile/Upload Arduino sketches
- Display Serial Connection for Arduino if there is
any data being displayed from the motor encoders.
- Calibrate Motors for further itrack-n-icatch operations
"""

# common
import re
import sys
import json
import uuid
from pathlib import Path
from datetime import datetime
from os import system, getcwd, scandir, chdir, path

import time # not currently used
import threading # use this later for running multiple tasks simultaniously

from send2trash import send2trash # required for the function `sendSketchToRecycleBin`
import winshell # required for the function `restoreSketch`

# Global variables
sketches_dir_name = "Sketches"
sketch_selected = "EmptySketch"
board_selected = "Arduino Uno"
fqbn_string = "arduino:avr:uno"
default_port = "COM3"

sketch_names = []

current_working_directory_path = getcwd()

def displayMenu(menu_items):
    """
    Display a menu where the key identifies the name of a 
    function.
    """
    print("\nAvailable Commands:")
    for index, (desc, _) in enumerate(menu_items, start=1):
        print(f"    {index} {desc}")

def showDevicesConnected():
    # Runs the arduino-cli command when
    # to display the show devices connected
    
    system(f"arduino-cli board list")

    return print("\n ")
    
def searchAllSketchesAvailable():
    # Search the dictionary `Sketches`
    # and show all the sketches available
    
    global sketches_dir_name
    
    sketch_names.clear()
    
    if current_working_directory_path: 
        sketches_path = chdir(sketches_dir_name)
    else:
        print("Problem in changing the directory path. Current Directory:", getcwd())
    
    names = [ f.name for f in scandir(sketches_path) if f.is_dir() ]
    
    sketch_names.extend(names)
    
    return sketch_names, chdir("..")
    
def createNewSketch():
    # create a new sketch with arduino-cli command
    # in the directory `Sketches`
    
    global sketches_dir_name
    
    sketches_path = chdir(sketches_dir_name)
    
    sketch_creating_name = input("Please enter name of the NEW SKETCH: ")
    
    system(f"arduino-cli sketch new {sketch_creating_name}")
    
    return chdir(".."), searchAllSketchesAvailable()

def sendSketchToRecycleBin():
    # Move the sketch directory to trash folder
    # inside the `Sketches` directory
    
    global sketches_dir_name
    global sketch_names
    
    sketch_trashing_name = input("Please enter name of the sketch to RECYCLE: ")
    
    if sketch_trashing_name.isdigit():
        raise ValueError
        
    # Check even if the sketch name exists
    if any(elem in sketch_trashing_name for elem in sketch_names):
        try:
            send2trash(f"{sketches_dir_name}\\{sketch_trashing_name}")
            
            sketch_path = f"{getcwd()}\\{sketches_dir_name}\\{sketch_trashing_name}"
            
            # Key is the current date and value is 
            # the sketch name being trashed
            
            sketch_trashed_with_ids = {str(uuid.uuid4()): {"date": datetime.now().strftime("%d-%m-%Y"), "path": sketch_path}}
        
            # If sketch trashed then store the name 
            # of the sketch trashed
            with open("sketch_trashed.json", "w", encoding="utf-8") as f:
                json.dump(sketch_trashed_with_ids, f, indent=4, ensure_ascii=False)
                
            print(f"Moved sketch named: {sketch_trashing_name} to recycle bin")
        except (OSError, IOError) as e:
            print(e)
    else:
        return print("Please choose an existing sketch to recycle.")
    
    return searchAllSketchesAvailable()
    
def restoreSketch():
    # Restore the sketch directory from the
    # trash folder back inside the `Sketches` directory
    
    updated_sketch_trashed = {}
    
    if path.getsize("sketch_trashed.json") > 0:
        try:
            with open("sketch_trashed.json", "r", encoding="utf-8") as f:
                loaded_sketch_trashed = json.load(f)
                
            if (bool(loaded_sketch_trashed)):
                print("Sketches currently in recycling bin: \n")
                s = "Index |"
                t = "Days Since Sketch Trashed |"
                a = "Sketch Path"
                print(f"{s:<20} {t:<20} {a}")
        
                try:
                    for idx, (unique_id, details) in enumerate(loaded_sketch_trashed.items(), start=1):
                        # Check if the sketch trashed still exists
                        # in the trash bin folder

                        found_trashed_sketch = True
                
                        for item in winshell.recycle_bin().versions(details["path"]):
                            original_path = str(item).split(" ")[0]
                            sketch_trashed_path = str(details["path"].lower())
                            if isinstance(original_path, str) == isinstance(sketch_trashed_path, str):
                                found_trashed_sketch = True
                                sketches_available_to_restore = []
                                sketches_available_to_restore.append(details["path"])
                                break
                            else:
                                pass
                
                        if found_trashed_sketch:
                            date_sketch_trashed = datetime.strptime(details["date"], "%d-%m-%Y")
                            current_time = datetime.now()
                            days_since_trashed_sketch = (current_time.date() - date_sketch_trashed.date()).days
                            
                            tem_idx = f"{idx}]"
                            print(f"    [{idx:<20} {str(days_since_trashed_sketch):<20} {details["path"]}")
                        else:
                            updated_sketch_trashed = loaded_sketch_trashed.pop(idx)
                    sketch_restoring_name = input("Please enter the number of the sketch path to RESTORE: ")
                
                    if not sketch_restoring_name.isdigit():
                        print("Invalid Input. Please enter a number")
                        return None
                
                    sketch_restoring_name = int(sketch_restoring_name)
                
                    if 1 <= sketch_restoring_name <= len(sketches_available_to_restore):
                        sketch_path_selected = sketches_available_to_restore[sketch_restoring_name - 1]
                        
                        r = list(winshell.recycle_bin())
                        paths = [re.search(r'([A-Za-z]:\\[^\r\n<>:"|?*]+)', str(item.original_filename)).group(1).strip().split(" ")[0] for item in r]
                        print(paths[1])
                        path_to_go = sketch_path_selected.replace('\\\\', '\\')                         
                        index = paths.index(path_to_go) 
                        
                        try:
                            winshell.undelete(r[index].original_filename())
                  
                            print(f"Restored the sketch: {sketch_path_selected}")
                            updated_sketch_trashed = loaded_sketch_trashed.pop(idx)
                        except Exception as e:
                            print(e)
                    else:
                        print("Invalid Selection. Please select from the list above.")
                
                except Exception as e:
                    print(e)
                
                
            else:
                pass
        except json.JSONDecodeError as e:
            print(e.msg, e.pos)
    else:
        print("Error prasing an empty json file.")
    
    if (bool(updated_sketch_trashed)):
        try:
            with open("sketch_trashed.json", "w", encoding="utf-8") as f:
                f.truncate() # clear the file's content
                json.dump(updated_sketch_trashed, f, indent=4, ensure_ascii=False)
        except OSError as e:
            print(e)
    else:
        return None
    
def selectSketch():
    # search the sketches availables
    # and select the default sketch
    
    global sketch_selected
    
    searchAllSketchesAvailable() # get available sketches names
    
    print("\nSelect Sketch:")
    
    for index, name in enumerate(sketch_names, start=1):
        print(f"    {index} {name}")
        
    print("\n    press n + enter to create a new sketch")
    print("    press d + enter to delete a sketch")
    print("    press r + enter to restore a sketch")
    print("    press e + enter to edit a sketch")
    print("    press b + enter to return to main menu")
    
    sketch_selected = input("")
    
    if not (
        sketch_selected.isdigit() 
        or sketch_selected == "n"
        or sketch_selected == "d"
        or sketch_selected == "r"
        or sketch_selected == "e"
        or sketch_selected == "b"
    ):
        raise ValueError
    
    if sketch_selected == "n":
        createNewSketch()
    elif sketch_selected == "d":
        sendSketchToRecycleBin()
    elif sketch_selected == "r":
        restoreSketch()
    elif sketch_selected == "e":
        editSketch()
    elif sketch_selected == "b":
        return None
    else:    
        sketch_selected = int(sketch_selected)
        
        if 1 <= sketch_selected <= len(sketch_names):
            sketch_name_selected = sketch_names[sketch_selected - 1]
            
            sketch_selected = sketch_name_selected
        else:
            print("\nInvalid choice. Please select a valid option.")
    
    return sketch_selected
    
def compileSketch():
    # Choose the default sketch selected to compile
    
    global sketch_selected
    global sketches_dir_name
    
    sketch_path = f"{sketches_dir_name}/{sketch_selected}"
    
    system(f"arduino-cli compile -b {fqbn_string} {sketch_path}")
    
    return print("\n ")

def uploadSketch():
    # Use default port and fqbn value
    # and try to upload the code
    
    global sketch_selected
    global sketches_dir_name
    global default_port
    
    sketch_path = f"{sketches_dir_name}/{sketch_selected}"
    
    system(f"arduino-cli upload {sketch_path} -p {default_port} -b {fqbn_string}")
    
    return print("\n ")
    
    return None
    
def itrackNicatch():
    # Run the associated Arduino sketch when
    # this function is called by the user
    
    # Reset the board + Adjust the placement of the robot
    # Test the motors
    # Calibrate motors encoders
    return None
    
def clear():
    system('cls')

def quit():
    sys.exit("Goodby")
    
def main():
    # list of tuples (function description, function name)
    menu_items = [
        ("show all connected boards", showDevicesConnected),
        ("edit / create / delete a sketch", selectSketch),
        ("compile the current sketch selected", compileSketch),
        ("upload the current sketch selected", uploadSketch),
        ("run itrack-n-icatch", itrackNicatch),
        ("clear the console", clear),
        ("quit this program", quit)
    ]
    
    while True:
        print(f"\nCurrent Working Directory: {getcwd()}") # display the sketch selected
        print(f"Sketch Selected: {sketch_selected} | Board Selected: {board_selected} | FQBN: {fqbn_string} | Default Port: {default_port}")
        
        displayMenu(menu_items)
        selection = input("") # Get function key
        
        if not selection.isdigit():
            print("\nInvalid input. Please enter a number.")
            continue
            
        selection = int(selection)
        
        if 1 <= selection <= len(menu_items):
            _, func = menu_items[selection - 1]
            func()
        else:
            print("\nInvalid choice. Please select a valid menu option.")
        
if __name__ == "__main__":
    main()