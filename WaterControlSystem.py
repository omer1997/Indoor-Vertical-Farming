#Created By Murad Sulieman
from tkinter import *
from NewSetupPumps import PumpSetup
from ManualPumpControl import LiveAdjustment
import csv
from pathlib import Path
from datetime import datetime, timedelta, time

#Class to encapsulate the main menu window and routines
class MainMenu:
    def __init__(self, master, geometry):
        #window setup
        self.master = master
        self.geometry = geometry
        self.master.geometry(self.geometry)
        self.master.title('Water Control System')
        self.title = Label(self.master, text="Water Control System")
        self.title.configure(fg='black',font=('Times',22))

        defaultbg = self.master.cget('bg')

        #Frame Setup
        Frame1 = LabelFrame(self.master,relief = 'flat', padx = 20 , pady = 10)
        Frame2 = LabelFrame(self.master, text = 'Current Setup', bd=3 , relief='raised', padx = 20 , pady = 10)
        #Frame3 = LabelFrame(self.master, text = 'Conditions', bd=3 , relief='raised', padx = 20 , pady = 10)

        #Frame1 buttons
        b1 = Button(Frame1, text = 'New Setup', width = 10, command = self.createNewSetup)
        b2 = Button(Frame1, text = 'Live Adjustment', command = self.manualOverride)
        b3 = Button(Frame1, text = 'Exit', command = self.master.destroy)

        #Frame 2 Labels
        self.DateVar = StringVar()
        dateLabel = Label(Frame2, text = 'Start Date:')
        self.dateText = Text(Frame2, state='disabled' ,width = 10, height = 1, bg = defaultbg, relief = 'flat')


        self.GrowCycleVar = StringVar()
        growCycleLabel = Label(Frame2, text = 'Length (days):')
        self.growCycleText = Text(Frame2, state='disabled' ,width = 2, height = 1, bg = defaultbg, relief = 'flat')


        self.OccurrenceVar = StringVar()
        ocurrenceLabel = Label(Frame2 , text = 'Occurrences:')
        self.occurrenceText = Text(Frame2, state='disabled' ,width = 5, height = 1, bg = defaultbg, relief = 'flat')


        self.ModeVar = StringVar()
        modeLabel = Label(Frame2, text = 'Mode:')
        self.modeText = Text(Frame2, state='disabled' ,width = 4, height = 1, bg = defaultbg, relief = 'flat')


        self.WaterCycleStartVar = StringVar()
        startTimeLabel = Label(Frame2, text = 'Water Cycle Start Time:')
        self.startTimeText = Text(Frame2, state='disabled' ,width = 5, height = 1, bg = defaultbg, relief = 'flat')


        self.DurationVar = StringVar()
        durationLabel = Label(Frame2, text = 'Duration (seconds):')
        self.durationText = Text(Frame2, state='disabled' ,width = 3, height = 1, bg = defaultbg, relief = 'flat')


        #Frame 3 Labels
        #pH = Label(Frame3, text = 'pH:')
        #phVar = StringVar()
        #DO = Label(Frame3, text = 'Dissolved Oxygen:')
        #DOVar = StringVar()
        #Con = Label(Frame3, text = 'Conductivity:')
        #ConVar = StringVar()
        #ORP = Label(Frame3 , text = 'ORP:')
        #ORPVar = StringVar()
        #Temp = Label(Frame3 , text = 'Temperature:')
        #TempVar = StringVar()

        #Frame 1 grid setup
        b1.grid(row = 1, column = 0, pady = 10)
        b2.grid(row = 2, column = 0, pady = 10)
        b3.grid(row = 3, column = 0, pady = 10)


        #Frame 2 grid setup
        dateLabel.grid(row = 0, column = 0, pady = 1, sticky = W)
        self.dateText.grid(row = 0, column = 1, pady = 3, sticky = E)

        growCycleLabel.grid(row = 1 , column = 0, pady = 1, sticky = W)
        self.growCycleText.grid(row = 1 , column = 1, pady = 3, sticky = E)

        ocurrenceLabel.grid(row = 2, column = 0, pady = 1, sticky = W)
        self.occurrenceText.grid(row = 2, column = 1, pady = 3, sticky = E)

        modeLabel.grid(row = 3, column = 0, pady = 1, sticky = W)
        self.modeText.grid(row = 3, column = 1, pady = 3, sticky = E)

        startTimeLabel.grid(row = 4 , column = 0, pady = 1, sticky = W)
        self.startTimeText.grid(row = 4 , column = 1, pady = 3, sticky = E)

        durationLabel.grid(row = 5, column = 0, pady = 1, sticky = W)
        self.durationText.grid(row = 5, column = 1, pady = 3, sticky = E)

        #Frame3 grid setup
        #pH.grid(row = 1 , column = 0, pady = 11)
        #DO.grid(row = 2 , column = 0, pady = 10)
        #Con.grid(row = 3, column = 0, pady = 10)
        #ORP.grid(row = 4, column = 0, pady = 10)
        #Temp.grid(row = 5, column = 0, pady = 12)

        #Grid setup
        self.title.grid(row = 0, column = 0, columnspan=6)
        Frame1.grid(row = 1, column = 0)
        Frame2.grid(row = 1, column = 1)
        #Frame3.grid(row = 1, column = 2)

        self.updateOverview()

    def createNewSetup(self):
        self.master.iconify()
        newWindow = Toplevel(self.master)
        newSetup = PumpSetup(newWindow)

    def manualOverride(self):
        self.master.iconify()
        newWindow = Toplevel(self.master)
        override = LiveAdjustment(newWindow)

    def updateOverview(self):
        file = Path.cwd() / "parameters.csv"
        if file.is_file():
            self.dateText['state'] = 'normal'
            self.growCycleText['state'] = 'normal'
            self.occurrenceText['state'] = 'normal'
            self.modeText['state'] = 'normal'
            self.startTimeText['state'] = 'normal'
            self.durationText['state'] = 'normal'

            with open('parameters.csv', mode='r') as csv_file:
                reader = csv.reader(csv_file)
                parameters = next(reader)



                self.GrowCycleVar.set(parameters[0])
                self.growCycleText.insert('end', self.GrowCycleVar.get())

                self.DateVar.set(parameters[1])
                self.dateText.insert('end', self.DateVar.get())
                if int(parameters[2]) == 1:
                    self.OccurrenceVar.set("Once")
                else:
                    self.OccurrenceVar.set("Twice")

                self.occurrenceText.insert('end', self.OccurrenceVar.get())

                if int(parameters[3]) == 1:
                    self.ModeVar.set("Farm")

                else:
                    self.ModeVar.set("Germ")

                self.modeText.insert('end', self.ModeVar.get())

                format_string = "%H:%M"
                startTime = datetime.strptime(parameters[4], format_string)
                startTime = startTime.time()
                self.WaterCycleStartVar.set(startTime)
                self.startTimeText.insert('end', self.WaterCycleStartVar.get())

                self.DurationVar.set(parameters[5])
                self.durationText.insert('end', self.DurationVar.get())


            self.dateText['state'] = 'disabled'
            self.growCycleText['state'] = 'disabled'
            self.occurrenceText['state'] = 'disabled'
            self.modeText['state'] = 'disabled'
            self.startTimeText['state'] = 'disabled'
            self.durationText['state'] = 'disabled'





def main():
    geometry = "500x300"
    root = Tk()
    mainMenu = MainMenu(root, geometry)
    root.mainloop()

if __name__ == '__main__':
    main()
