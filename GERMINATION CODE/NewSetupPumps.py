#created by Murad Sulieman

from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import csv

class PumpSetup:
    def __init__(self, master):
        #self.master Setup
        self.master = master
        self.master.title('New Setup')
        self.title = Label(self.master, text = 'New Setup')
        self.title.configure(fg='black',font=('Times',22 ,'underline'), pady = 10)


        #Entry for the amount of days for growth cycle
        self.growthLength = StringVar()
        growthLabel = Label(self.master, text = 'Grow Cycle Length (Days):')
        growthEntry = Entry(self.master, width = 5, textvariable = self.growthLength)


        #this sets the date and time for the growth cycle

        self.startDate = StringVar()
        dateLabel = Label(self.master, text = "Enter Start Date (mm/dd/yyyy): ")
        dateEntry = Entry(self.master, width = 10, textvariable = self.startDate)



        #time setup
        timeLabel = Label(self.master, text = 'Start Time:')
        self.hour = StringVar()
        hourbox = ttk.Combobox(self.master, width = 3 , textvariable = self.hour)
        hourbox['values'] = list(range(0,24))
        hourbox.current()

        self.minutes = StringVar()
        minutesbox = ttk.Combobox(self.master, width = 3, textvariable = self.minutes)
        minutesbox['values'] = list(range(00,60,5))
        minutesbox.current()



        #Occurrences
        ocurrenceLabel = Label(self.master, text = 'Occurrences:')
        self.occurrences = IntVar()
        once = Radiobutton(self.master, text = "Once", variable = self.occurrences, value = 1)
        twice = Radiobutton(self.master, text = "Twice", variable = self.occurrences, value = 2)




        #mode selection
        modeLabel = Label(self.master, text = 'Mode:')
        self.modeState = IntVar()
        #farmMode = Radiobutton(self.master, text = "Farm", variable = self.modeState, value = 1)
        germMode = Radiobutton(self.master, text = "Germination", variable = self.modeState, value = 2)


        #duration
        durationLabel = Label(self.master, text = 'Duration(seconds):')
        self.duration = StringVar()
        durationEntry = Entry(self.master, width = 3, textvariable = self.duration)

        #submit button
        SubmitButton = Button(self.master, text = 'Submit', command = self.submitSetup)

        #Grid setup
        self.title.grid(row = 0, column = 0, columnspan = 5)

        growthLabel.grid(row = 1, column = 0, pady = 5)
        growthEntry.grid(row = 1, column = 1, pady = 5)

        dateLabel.grid(row = 2, column = 0, sticky=(W), pady = 6)
        dateEntry.grid(row = 2, column = 1, sticky=(W), pady = 6)

        ocurrenceLabel.grid(row = 3, column = 0, pady = 5)
        once.grid(row = 3, column = 1, pady = 5)
        twice.grid(row = 3, column = 2, pady = 5)

        timeLabel.grid(row = 4 , column = 0, pady = 5)
        hourbox.grid(row = 4 , column = 1, pady = 5)
        minutesbox.grid(row = 4 , column = 2, pady = 5)


        modeLabel.grid(row = 5, column = 0, pady = 5)
        #farmMode.grid(row = 5 , column = 1, pady = 5)
        germMode.grid(row = 5, column = 2, pady = 5)

        durationLabel.grid(row = 6, column = 0, pady = 5)
        durationEntry.grid(row = 6, column = 1, pady = 5)

        SubmitButton.grid(row = 7, column = 0, columnspan = 6)

    def submitSetup(self):
        self.writeToCSV()
        self.master.destroy()

    def writeToCSV(self):
        parameters = []
        parameters.append(self.growthLength.get())
        parameters.append(self.startDate.get())
        parameters.append(self.occurrences.get())
        parameters.append(self.modeState.get())
        parameters.append(self.hour.get() + ":" + self.minutes.get())
        parameters.append(self.duration.get())

        with open('parameters.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(parameters)
