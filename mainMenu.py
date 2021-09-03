from tkinter import *
from SetupView import SetupWindow


class MainMenu:
    def __init__(self, master, geometry):
        self.master = master
        self.geometry = geometry
        self.master.geometry(self.geometry)

        self.frame = Frame(self.master)
        self.frame.pack()


        self.label = Label(self.frame, text = "Main Menu")
        self.label.pack()

        self.button1 = Button(text = "Create New Cycle", command = self.createGrowCycle)
        self.button1.pack(padx = 3, pady = 3)
        self.button2 = Button(text = "Import Existing Cycle")
        self.button2.pack(padx = 3, pady = 3)
        self.button3 = Button(text = "View Active Cycle")
        self.button3.pack(padx = 3, pady = 3)
        self.button4 = Button(text = "Modify Active Cycle")
        self.button4.pack(padx = 3, pady = 3)
        self.button5 = Button(text = "Exit")
        self.button5.pack(padx = 3, pady = 3)

        self.master.title("Vertical Farm Lighting Controls")


    def createGrowCycle(self):
        self.master.iconify()
        self.newWindow = Toplevel(self.master)
        self.createNew = SetupWindow(self.newWindow, self.geometry)





def main():
    geometry = "550x600"
    root = Tk()
    mainMenu = MainMenu(root, geometry)
    root.mainloop()

if __name__ == '__main__':
    main()
