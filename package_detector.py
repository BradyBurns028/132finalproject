#############################################################
# Test 3 of Arduino and Python communication:
# IR sensor detecting package
#############################################################

import serial
import time

arduino = serial.Serial(port="COM3", baudrate=9600, timeout=.1)
time.sleep(2)

while True:
    line = arduino.readline()
    if line:
        string = line.decode()
        num = int(string)
        if (num == 1):
            detector = False
        else:
            detector = True
    print(detector)
    time.sleep(1)