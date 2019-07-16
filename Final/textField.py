from tkinter import *
from tkinter import font, SUNKEN, Scrollbar

class dailyJournal(Frame):

    def __init__(self,master):

        Frame.__init__(self,master)


        self.grid()
        self.t2 = Text(width=50, font=("Courier",14))
        self.t2.grid(row = 1,column=0, sticky = N + S + E + W)

        self.t1 = Text(width=50, font=("Courier",14))
        self.t1.grid(row = 1,column=1, sticky = N + S + E + W)

        self.scrollbar = Scrollbar(root)
        self.scrollbar.grid(row= 1,column = 1, sticky = N + S + E)
        self.scrollbar.config(command = self.t1.yview)

        self.t3 = Text(width=50, font=("Courier",14))
        self.t3.grid(row = 1,column=2, sticky = N + S + E + W)


        self.titletag = Label(master, text = "Entry Title: ", relief = SUNKEN, font = ("Times", 14)).grid(row= 0, column = 0, sticky=NE)
        self.titleentry = Entry(master, font=("Courier", 14),).grid(row = 0, column = 1, ipadx = 164)


        menu = Menu(root)
        menu.add_command(label="New")
        menu.add_command(label="Save")
        menu.add_command(label="Save As")
        menu.add_command(label="Open")
        root.config(menu=menu)

root = Tk()
app = dailyJournal(root)
root.geometry()
root.mainloop()