import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import*

class Journal:

    root = Tk()

    windowidth = 800
    windowheight = 600
    textarea = Text(root)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    editmenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)

    scrollbar = Scrollbar(textarea)
    file = None

journal = Journal(width=800,height=600)
journal.run()