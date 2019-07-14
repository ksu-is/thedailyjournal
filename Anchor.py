from tkinter import *

class dailyJournal(Frame):

    def __init__(self,master):

        Frame.__init__(self,master)


        self.grid()
        self.t1 = Text(width=32, font=("Brush Script MT",25))
        self.t1.grid(row = 0,column=0)

        self.t1 = Text(width=32, font=("Brush Script MT",25))
        self.t1.grid(row = 0,column=1)

        self.t1 = Text(width=32, font=("Brush Script MT",25))
        self.t1.grid(row = 0,column=2)
        
root = Tk()
app = dailyJournal(root)
root.geometry()
root.mainloop()