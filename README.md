# itrack-n-icatch: real time ball catching system

Developing a command line interface for Arduino that helps with:
- managing arduino sketches, enables selecting a default sketch that could be compiled, uploaded, edited, or deleted, and
  letting you restor recent sketches from trash.
- managing arduino libraries.

Bugs:
- the default sketch changes even when user inputs a number, or a letter (e, n, p) for other commands (editing, deleting, 
  or reslorting the sketch).
- the application exits with a value error when inputed a number for option 3 (managing arduino libaries).

Potential improvements:
- Option to select a default arduino board from all the arduino boards connected to the device.
- Option selection changed from numbers to letters ( 1 --> press d + enter ).
- Once a default sketch is selected then you can delete or edit that sketch instead of seleting a sketch each time to delete
  or edit.
- Store the last default sketch selected by the user to keep the same one when the application is quitted and re-started.
