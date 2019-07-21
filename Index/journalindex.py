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

        self.root.geometry('%dx%d+%d+%d' % (self.windowwidth, self.windowheight, alignleft, aligntop))
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.textarea.grid(sticky = N + E + S + W)

        self.filemenu.add_command(label="New", command=self.newfile)

        self.filemenu.add_command(label="Open", command=self.openfile)

        self.filemenu.add_command(label="Save", command=self.savefile)

        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quitapplication)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu.add_command(label="Copy", command=self.copyselection)

        self.editmenu.add_command(label="Paste", command=self.pasteselection)

        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu.add_command(label="About Journal", command=self.showabout)

        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root.config(menu=self.menubar)

        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.scrollbar.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scrollbar.set)
    
    def quitapplication(self):
        self.root.destroy()
    
    def showabout(self):
        showinfo("Journal", "Build strong habits for a better you. Coder: Aleksandr Yeger w/ References")

    def openfile(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])

        if self.file == "":
            self.file = None

        else:
            self.root.title(os.path.basename(self.file) + " - Journal")
            self.textarea.delete(1.0,END)

            file = open(self.file,"r")

            file.close()

    def newfile(self):
        self.root.title("Untitled - Journal")
        self.file = None
        self.textarea.delete(1.0,END)

    def savefile(self):
        
        if self.file == None:
            self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.file == "":
                self.file = None
            else:
                file = open(self.file,"w")
                file.write(self.textarea.get(1.0,END))
                file.close()

                self.root.title(os.path.basename(self.file) + " - Journal")

        else:
            file = open(self.file,"w")
            file.write(self.textarea.get(1.0,END))
            file.close()

    def cutselection(self):
        self.textarea.event_generate("<<Cut>>")

    def copyselection(self):
        self.textarea.event.generate("<<Copy>>")

    def pasteselection(self):
        self.textarea.event_generate("<<Paste>>")

    def run(self):
        self.root.mainloop()    





journal = Journal(width=800,height=600)
journal.run()