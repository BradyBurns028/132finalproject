from tkinter import *
from datetime import datetime
import serial
import time
import RPi.GPIO as GPIO
import pygame

class GUI(Frame):
    def __init__(self, win):
        Frame.__init__(self, win, bg = "white")
        win.attributes("-fullscreen", True)
        self.setupGUI()
    
    def setupGUI(self):
        global newCode
        newCode = False
        global code
        code = "1234"   #default code
        global tempON
        tempON = False  #fans on or off
        global armed
        armed = False   #armed or not
        global curTemp
        curTemp = 70    #will update with sensor
        global goalTemp
        goalTemp = 50   #goal temp. Will adjust with testing
        global packTime
        packTime = datetime.now()
        
        
        #display
        self.display = Label(self, text = "", anchor = E, bg = "white", height = 1)
        self.display.grid(row = 0, column = 0, columnspan = 3, sticky = E+W+N+S)
        
        #1
        GUI.button1 = Button(self, width = 9, bg = "white", text = "1", borderwidth = 1, command = lambda: self.type("1"))
        GUI.button1.grid(row = 1, column = 0, stick = N+S+E+W)
        
        #2
        GUI.button2 = Button(self, width = 9, bg = "white", text = "2", borderwidth = 1, command = lambda: self.type("2"))
        GUI.button2.grid(row = 1, column = 1, stick = N+S+E+W)
        
        #3
        GUI.button3 = Button(self, width = 9, bg = "white", text = "3", borderwidth = 1, command = lambda: self.type("3"))
        GUI.button3.grid(row = 1, column = 2, stick = N+S+E+W)
        
        #4
        GUI.button4 = Button(self, bg = "white", text = "4", borderwidth = 1, command = lambda: self.type("4"))
        GUI.button4.grid(row = 2, column = 0, stick = N+S+E+W)
        
        #5
        GUI.button5 = Button(self, bg = "white", text = "5", borderwidth = 1, command = lambda: self.type("5"))
        GUI.button5.grid(row = 2, column = 1, stick = N+S+E+W)
        
        #6
        GUI.button6 = Button(self, bg = "white", text = "6", borderwidth = 1, command = lambda: self.type("6"))
        GUI.button6.grid(row = 2, column = 2, stick = N+S+E+W)
        
        #7
        GUI.button7 = Button(self, bg = "white", text = "7", borderwidth = 1, command = lambda: self.type("7"))
        GUI.button7.grid(row = 3, column = 0, stick = N+S+E+W)
        
        #8
        GUI.button8 = Button(self, bg = "white", text = "8", borderwidth = 1, command = lambda: self.type("8"))
        GUI.button8.grid(row = 3, column = 1, stick = N+S+E+W)
        
        #9
        GUI.button9 = Button(self, bg = "white", text = "9", borderwidth = 1, command = lambda: self.type("9"))
        GUI.button9.grid(row = 3, column = 2, stick = N+S+E+W)
        
        #clear
        GUI.clear = Button(self, bg = "white", text = "clear", borderwidth = 1, command = lambda: self.type(""))
        GUI.clear.grid(row = 4, column = 0, stick = N+S+E+W)
        
        #0
        GUI.button0 = Button(self, bg = "white", text = "0", borderwidth = 1, command = lambda: self.type("0"))
        GUI.button0.grid(row = 4, column = 1, stick = N+S+E+W)
        
        #reset
        GUI.reset = Button(self, bg = "white", text = "reset", borderwidth = 1, command = self.reset)
        GUI.reset.grid(row = 4, column = 2, stick = N+S+E+W)
        
        #temp on/off
        GUI.tempCtrl = Button(self, bg = "white", text = "Temp OFF", borderwidth = 1, command = lambda: self.temp())
        GUI.tempCtrl.grid(row = 5, column = 0, stick = N+S+E+W)
        
        #test button to arm system. Eventually will arm automatically
        #GUI.arms = Button(self, bg = "white", text = "", borderwidth = 1, command = lambda: self.arm())
        #GUI.arms.grid(row = 5, column = 1, stick = N+S+E+W)
        
        #display whether or not the system is armed
        GUI.isArmed = Label(self, bg = "green", text = "Safe", borderwidth = 1, relief = "raised")
        GUI.isArmed.grid(row = 5, column = 2, stick = N+S+E+W)
        
        #label for current temp
        GUI.tempLabel = Label(self, bg = "white", text = "Temp", borderwidth = 1, relief = "raised")
        GUI.tempLabel.grid(row = 6, column = 0, stick = N+S+E+W)
        
        #current temp number
        GUI.cTemp = Label(self, bg = "white", text = str(curTemp), borderwidth = 1, relief = "raised")
        GUI.cTemp.grid(row = 6, column = 1, stick = N+S+E+W)
        
        #label for goal temp
        GUI.goalLabel = Label(self, bg = "white", text = "Goal", borderwidth = 1, relief = "raised")
        GUI.goalLabel.grid(row = 7, column = 0, stick = N+S+E+W)
        
        #goal temp number
        GUI.gTemp = Label(self, bg = "white", text = str(goalTemp), borderwidth = 1, relief = "raised")
        GUI.gTemp.grid(row = 7, column = 1, stick = N+S+E+W)
        
        #Shows whether or not a package has been delivered and at what time.
        GUI.bottom = Label(self, bg = "white", text = "Package delivered at 12:00", borderwidth = 1, relief = "raised")
        GUI.bottom.grid(row = 8, column = 0, columnspan = 3, stick = N+S+E+W)
        
        for row in range(8):
            Grid.rowconfigure(self, row, weight = 1)
        for col in range(3):
            Grid.columnconfigure(self, col, weight = 1)
            
        self.pack(fill = BOTH, expand = 1)
        
    def type(self, str):
        global newCode
        global code
        text = self.display["text"]
        
        if(len(str)>0 and len(text) < 4 and newCode == False):
            if(len(code) < 4):
                code += str
            text += str
        else:
            if(newCode == True):
                code = str
                newCode = False
            text = str
        self.display["text"] = text
        
    def temp(self):
        global tempON
        tempON = not(tempON)
    
    def arm(self):
        global armed
        global packTime
        if(armed == False):
            packTime = datetime.now()
        armed = True
        
    def reset(self):
        global armed
        if(not armed):
            self.display["text"] = "Input new passcode"
            global newCode
            newCode = True
        
    
    def readCode(self):
        global code
        text = self.display["text"]
        if(text == code and len(code) == 4):
            global armed
            armed = False
            self.display["text"] = ""
            GPIO.output(25, GPIO.HIGH)
            time.sleep(0.5)
        
pygame.init()       
pygame.mixer.init()
alarmsound = pygame.mixer.Sound("alarm.wav")
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
window = Tk()
window.title("KEYPAD")
k = GUI(window)
global newCode
global code        
global tempON
global armed
global curTemp
global goalTemp
global packTime
arduino = serial.Serial(port="/dev/ttyACM0", baudrate=115200, timeout=.1)
time.sleep(2)

while(True):
    line = arduino.readline()
    string = line.decode()
    data = string.split(",")
    
    if len(data) == 3:
        curTemp = float(data[2])
        moved = int(data[1])
        detected = int(data[0])
        
        if(detected == 1):
            GUI.arm(k)
        if(moved == 1 and armed == True):
            pygame.mixer.music.load("alarm.wav")
            pygame.mixer.music.play()
        if(moved == 0):
            pygame.mixer.music.stop()
            
                         
    GUI.readCode(k)
    print("newCode T/F: {}".format(newCode))
    print("code: {}".format(code))
    print("tempON: {}".format(tempON))
    print("armed: {}".format(armed))         
    print("curTemp: {}".format(curTemp))
    print("goalTemp: {}".format(goalTemp))
    print("packTime: {}".format(packTime))
    
    
    #Add method to change curTemp to a value read from PIN
    GUI.cTemp.config(text = curTemp)
    
    if(armed):
        GUI.isArmed.config(text = "Armed", bg = "red")
        GUI.bottom.config(text = "Package delivered at {}".format(packTime.strftime("%H:%M:%S")))
    else:
        GUI.isArmed.config(text = "Safe", bg = "green")
        GUI.bottom.config(text = "No package detected")
        GPIO.output(25, GPIO.LOW)        
    if(tempON):
        GUI.tempCtrl.config(text = "Temp On")
        GPIO.output(17, GPIO.HIGH)
    else:
        GUI.tempCtrl.config(text = "Temp Off")
        GPIO.output(17, GPIO.LOW)
    
    window.update()

window.mainloop()
    
        