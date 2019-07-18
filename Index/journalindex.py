import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import*

class Journal:

    root = Tk()

    windowwidth = 800
    windowheight = 600
    textarea = Text(root)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    editmenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)

    scrollbar = Scrollbar(textarea)
    file = None

    def __init__(self,**kwargs):

        self.windowwidth = kwargs['width']
        self.windowheight = kwargs['height']

        self.root.title("Untitled - Journal Entry")

        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        alignleft = (screenWidth / 2) - (self.windowwidth /2)

        aligntop = (screenHeight /2) - (self.windowheight /2)

        self.root.geometry('%dx%dx+%dx%dx' % (self.windowwidth, self.windowheight, alignleft, aligntop))
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.textarea.grid(sticky = N + E + S + W)

journal = Journal(width=800,height=600)
journal.run()