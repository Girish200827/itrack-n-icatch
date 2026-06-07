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
import sys
import signal
from os import system, getcwd, scandir, chdir

import time # not currently used
import threading # use this later for running multiple tasks simultaniously

# Global variables
sketches_dir = "Sketches"
sketch_selected = "EmptySketch"
board_selected = "Arduino Uno"
fqbn_string = "arduino:avr:uno"
default_port = "Comp3"

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
    
def searchAllSketchsAvailable():
    # Search the dictionary `Sketches`
    # and show all the sketches available
    
    global sketches_dir
    
    sketch_names.clear()
    
    if current_working_directory_path: 
        sketches_path = chdir(sketches_dir)
    else:
        print("Problem in changing the directory path. Current Directory:", getcwd())
    
    names = [ f.name for f in scandir(sketches_path) if f.is_dir() ]
    
    sketch_names.extend(names)
    
    return sketch_names, chdir("..")
    
def createNewSketch():
    # create a new sketch with arduino-cli command
    # in the directory `Sketches`
    
    return None

def deleteSketch():
    # move the sketch directory to trash folder
    # inside the `Sketches` directory
    
    return None

def restoreSketch():
    # restore the sketch directory from the
    # trash folder back inside the `Sketches` directory
    
    return None

def selectSketch():
    # search the sketches availables
    # select the sketch
    
    global sketch_selected
    
    searchAllSketchsAvailable() # get available sketches names
    
    print("\nSelect Sketch:")
    
    for index, name in enumerate(sketch_names, start=1):
        print(f"    {index} {name}")
        
    print("\n    press n + enter to create a new sketch")
    print("    press d + enter to delete a sketch")
    print("    press r + enter to restore a sketch")
    
    sketch_selected = input("")
    
    if not (
        sketch_selected.isdigit() 
        or sketch_selected == "n"
        or sketch_selected == "d"
        or sketch_selected == "r"
    ):
        return print("\nInvalid input. Please enter a number.")
    
    if sketch_selected == "n":
        createNewSketch()
        return None
    elif sketch_selected == "d":
        deleteSketch()
        return None
    elif sketch_selected == "r":
        restoreSketch()
        return None
    else:    
        sketch_selected = int(sketch_selected)
        
    if 1 <= sketch_selected <= len(sketch_names):
        sketch_name_selected = sketch_names[sketch_selected - 1]
    else:
        print("\nInvalid choice. Please select a valid option.")
        
    sketch_selected = sketch_name_selected
    
    return sketch_selected
    
def compileSketch():
    # Choose the default sketch selected to compile
    
    global sketch_selected
    global sketches_dir
    
    sketch_path = f"{sketches_dir}/{sketch_selected}"
    
    system(f"arduino-cli compile -b {fqbn_string} {sketch_path}")
    
    return print("\n ")

def uploadSketch():
    # Use default port and fqbn value
    # and try to upload the code
    
    global sketch_selected
    global sketches_dir
    global default_port
    
    sketch_path = f"{sketches_dir}/{sketch_selected}"
    
    system(f"arduino-cli upload {sketch_path} -p {default_port} -b {fqbn_string}")
    
    return print("\n ")
    
    return None

def editSketch():
    # Run the associated windows command when
    # this function is called by the user
    return None
    
def itrackNicatch():
    # Run the associated Arduino sketch when
    # this function is called by the user
    
    # Reset the board + Adjust the placement of the robot
    # Test the motors
    # Calibrate motors encoders
    return None
    
def sketchSelected():
    # Update the sketch selected
    # use threading here
    
    return None

def boardSelected():
    # Update the board selected
    # use threading here
    
    return None
    
def clear():
    system('cls')

def quit():
    sys.exit("Goodby")
    
def main():
    # list of tuples (function description, function name)
    menu_items = [
        ("show all connected boards", showDevicesConnected),
        ("select sketch from the available sketches", selectSketch),
        ("compile the current sketch selected", compileSketch),
        ("upload the current sketch selected", uploadSketch),
        ("edit the current sketch selected", editSketch),
        ("run itrack-n-icatch", itrackNicatch),
        ("clear the console", clear),
        ("quit this program", quit)
    ]
    
    while True:
        print(f"Current Working Directory: {getcwd()}") # display the sketch selected
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