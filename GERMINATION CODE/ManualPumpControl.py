 # Manual Pump Control GUI created by Khasim Rizvi, based on code/support from Nehemiah Myers and Murad Suleiman
from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#farmPumps = 2
germPumps = 26

GPIO.setwarnings(False)

#GPIO.setup(farmPumps, GPIO.OUT)
GPIO.setup(germPumps, GPIO.OUT)



class LiveAdjustment:
    def __init__(self, master):
        # Establish self.master
        self.master = master
        self.master.title('Manual Control')  # Establish window Title

        # Establish Title Label
        self.title = Label(self.master, text="Live Adjustment")
        self.title.configure(fg='black', font=('Times', 18))

        # Establishing Buttons
        #bFOn = Button(self.master, text="Farm Pump On", bg="Green", fg="Black", command = self.farmPumpOn)  # Turn Farm Pumps On
        bGOn = Button(self.master, text="Germination Pump On", bg="Green", fg="Black", command = self.germPumpOn)  # Turn Farm Pumps Off
        #bFOff = Button(self.master, text="Farm Pump Off", bg="Red", fg="Black", command = self.farmPumpOff)  # Turn Germ Pump Off
        bGOff = Button(self.master, text="Germination Pump Off", bg="Red", fg="Black", command = self.germPumpOff)  # Turn Germ Pump Off
        bBack = Button(self.master, text="Exit", fg="Black", command = lambda:[GPIO.cleanup(), self.master.destroy()])  # Exit Button closes the current window

        # Placement of Buttons and Title
        self.title.grid(row=0,column=0,columnspan=4)
        #bFOn.grid(row=5,column=0, sticky=W+E, columnspan=2, pady=5, padx=5)
        bGOn.grid(row=10,column=0, sticky=W+E, columnspan=2, pady=5, padx=5)
        bBack.grid(row=15,column=0, columnspan=4, pady=5, padx=5)
        #bFOff.grid(row=5,column=2, sticky=W+E, pady=5, padx=5)
        bGOff.grid(row=10,column=2, sticky=W+E, pady=5, padx=5)

    #Relay Outlet Module is Active LOW
    #def farmPumpOn(self):

        #GPIO.output(farmPumps, GPIO.HIGH)

    #def farmPumpOff(self):

        #GPIO.output(farmPumps, GPIO.LOW)

    def germPumpOn(self):

        GPIO.output(germPumps, GPIO.HIGH)

    def germPumpOff(self):

        GPIO.output(germPumps, GPIO.LOW)
