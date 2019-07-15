from tkinter import *
from tkinter import font, SUNKEN

class dailyJournal(Frame):

    def __init__(self,master):

        Frame.__init__(self,master)


        self.grid()
        self.t1 = Text(width=50, font=("Courier",14))
        self.t1.grid(row = 1,column=0)

        self.t1 = Text(width=50, font=("Courier",14))
        self.t1.grid(row = 1,column=1)

        self.t1 = Text(width=50, font=("Courier",14))
        self.t1.grid(row = 1,column=2)


        self.titletag = Label(master, text = "Entry Title: ", relief = SUNKEN, font = ("Times", 14)).grid(row= 0, column = 0, sticky=NE)
        self.titleentry = Entry(master, font=("Courier", 14),).grid(row = 0, column = 1, ipadx = 164)

root = Tk()
app = dailyJournal(root)
root.geometry()
root.mainloop()