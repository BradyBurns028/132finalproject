#############################################################
# Test 1 of Arduino and Python communication:
# GUI to turn ON/OFF LED connected to Arduino
#############################################################

from tkinter import *
from pyfirmata import Arduino

# Arduino board connected to serial port COM3
board = Arduino("COM3")

# Functions
def ledON():
    # LED connected to digital pin 3, 1 means HIGH
    board.digital[3].write(1)
def ledOFF():
    # LED connected to digital pin 3, 0 means LOW
    board.digital[3].write(0)

# initialize window
window = Tk()
window.title("L E D")
window.minsize(200,60)

# Label widget
label = Label(window, text="click to turn ON/OFF")
label.grid(column=1, row=1)

# Button widget
on = Button(window, bd=4, text="LED ON", command=ledON)
on.grid(column=1, row=2)
off = Button(window, bd=4, text="LED OFF", command=ledOFF)
off.grid(column=2, row=2)

window.mainloop()