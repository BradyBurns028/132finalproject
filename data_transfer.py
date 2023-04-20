#############################################################
# Test 2 of Arduino and Python communication:
# Collect values read/printed out in Arduino's serial monitor
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
        print(num)
