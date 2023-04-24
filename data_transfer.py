#############################################################
# Test 2 of Arduino and Python communication:
# Collect values read/printed out in Arduino's serial monitor
#############################################################
import serial
import time

arduino = serial.Serial(port="COM3", baudrate=115200, timeout=.1)
time.sleep(2)

while True:
    line = arduino.readline()
    if line:
        string = line.decode()
        data = string.split(",")
        detected = int(data[0])
        moved = int(data[1])
        temperature = float(data[2])

        if moved == 1:
            # sound the piezo alarm
            pass
        if detected == 1:
            # show the box is locked on GUI
            pass

        # display temperature on GUI
        print(f"Detected = {detected}\tMoved = {moved}\tTemperature = {temperature}")
