# Import the GUI module (tkinter)
from tkinter import *

# Create an output window
root = Tk()

root.title('Button App') # Title of the app
 
root.geometry('600x600') # Size of the app

# If side = LEFT/RIGHT will align item center vertically. Default value: TOP
# If side = TOP/BOTTOM will align item center horizontally

# If expand = YES, will align the item center horizontally and vertically
# expand also expands its main axis. And its cross-axis if possible(?)
Button(root, text = 'A').pack(side = LEFT,
                              expand = YES,
                              fill = Y)

Button(root, text = 'B').pack(expand = YES,
                              fill = BOTH)

Button(root, text = 'C').pack(side = RIGHT, 
                              expand = YES,
                              fill = NONE,
                              anchor = NE)


Button(root, text = 'D').pack(side = RIGHT, #RIGHT/BOTTOM have the same effect
                              expand = NO,
                              fill = NONE)


# This will run the codes written before this code
root.mainloop()
