from tkinter import *
from _datetime import datetime

class GUI(Frame):
    def __init__(self, win):
        Frame.__init__(self, win, bg = "white")
        win.attributes("-toolwindow", True)
        self.setupGUI()
    
    def setupGUI(self):
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
        button1 = Button(self, width = 9, bg = "white", text = "1", borderwidth = 1, command = lambda: self.type("1"))
        button1.grid(row = 1, column = 0, stick = N+S+E+W)
        
        #2
        button2 = Button(self, width = 9, bg = "white", text = "2", borderwidth = 1, command = lambda: self.type("2"))
        button2.grid(row = 1, column = 1, stick = N+S+E+W)
        
        #3
        button3 = Button(self, width = 9, bg = "white", text = "3", borderwidth = 1, command = lambda: self.type("3"))
        button3.grid(row = 1, column = 2, stick = N+S+E+W)
        
        #4
        button4 = Button(self, bg = "white", text = "4", borderwidth = 1, command = lambda: self.type("4"))
        button4.grid(row = 2, column = 0, stick = N+S+E+W)
        
        #5
        button5 = Button(self, bg = "white", text = "5", borderwidth = 1, command = lambda: self.type("5"))
        button5.grid(row = 2, column = 1, stick = N+S+E+W)
        
        #6
        button6 = Button(self, bg = "white", text = "6", borderwidth = 1, command = lambda: self.type("6"))
        button6.grid(row = 2, column = 2, stick = N+S+E+W)
        
        #7
        button7 = Button(self, bg = "white", text = "7", borderwidth = 1, command = lambda: self.type("7"))
        button7.grid(row = 3, column = 0, stick = N+S+E+W)
        
        #8
        button8 = Button(self, bg = "white", text = "8", borderwidth = 1, command = lambda: self.type("8"))
        button8.grid(row = 3, column = 1, stick = N+S+E+W)
        
        #9
        button9 = Button(self, bg = "white", text = "9", borderwidth = 1, command = lambda: self.type("9"))
        button9.grid(row = 3, column = 2, stick = N+S+E+W)
        
        #clear
        clear = Button(self, bg = "white", text = "clear", borderwidth = 1, command = lambda: self.type(""))
        clear.grid(row = 4, column = 0, stick = N+S+E+W)
        
        #0
        button0 = Button(self, bg = "white", text = "0", borderwidth = 1, command = lambda: self.type("0"))
        button0.grid(row = 4, column = 1, stick = N+S+E+W)
        
        #reset
        reset = Button(self, bg = "white", text = "reset", borderwidth = 1, command = lambda: self.type("reset"))
        reset.grid(row = 4, column = 2, stick = N+S+E+W)
        
        #temp on/off
        tempCtrl = Button(self, bg = "white", text = "Temp OFF", borderwidth = 1, command = lambda: self.temp())
        tempCtrl.grid(row = 5, column = 0, stick = N+S+E+W)
        
        #test button to arm system. Eventually will arm automatically
        arms = Button(self, bg = "white", text = "", borderwidth = 1, command = lambda: self.arm())
        arms.grid(row = 5, column = 1, stick = N+S+E+W)
        
        #display whether or not the system is armed
        isArmed = Label(self, bg = "green", text = "Safe", borderwidth = 1, relief = "raised")
        isArmed.grid(row = 5, column = 2, stick = N+S+E+W)
        
        #label for current temp
        tempLabel = Label(self, bg = "white", text = "Temp", borderwidth = 1, relief = "raised")
        tempLabel.grid(row = 6, column = 0, stick = N+S+E+W)
        
        #current temp number
        cTemp = Label(self, bg = "white", text = str(curTemp), borderwidth = 1, relief = "raised")
        cTemp.grid(row = 6, column = 1, stick = N+S+E+W)
        
        #label for goal temp
        goalLabel = Label(self, bg = "white", text = "Goal", borderwidth = 1, relief = "raised")
        goalLabel.grid(row = 7, column = 0, stick = N+S+E+W)
        
        #goal temp number
        gTemp = Label(self, bg = "white", text = str(goalTemp), borderwidth = 1, relief = "raised")
        gTemp.grid(row = 7, column = 1, stick = N+S+E+W)
        
        #Shows whether or not a package has been delivered and at what time.
        pack = Label(self, bg = "white", text = "Package delivered at 12:00", borderwidth = 1, relief = "raised")
        pack.grid(row = 8, column = 0, columnspan = 3, stick = N+S+E+W)
        
        for row in range(8):
            Grid.rowconfigure(self, row, weight = 1)
        for col in range(3):
            Grid.columnconfigure(self, col, weight = 1)
            
        self.pack(fill = BOTH, expand = 1)
        
    def type(self, str):
        text = self.display["text"]
        
        if(len(str)>0):
            text += str
        else:
            text = str
        self.display["text"] = text
        
    def temp(self):
        global tempON
        tempON = not(tempON)
    
    def arm(self):
        global armed
        armed = True
        global packTime
        packTime = datetime.now()
        
    def reset(self):
        pass
        
    
window = Tk()
window.title("KEYPAD")
k = GUI(window)
window.mainloop()
        