import tkinter
import os
import webbrowser
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import*

class Journal:

    root = Tk()


    #base window dementions
    windowwidth = 800
    windowheight = 600
    textarea = Text(root)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    editmenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)

    #for adding scrollbar later
    scrollbar = Scrollbar(textarea)
    file = None

    def __init__(self,**kwargs):
        
        #for setting the window dementions stated earlier
        self.windowwidth = kwargs['width']
        self.windowheight = kwargs['height']

        #default window text
        self.root.title("Untitled - Journal Entry")

        #centering the window at launch
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        #left-aligning
        alignleft = (screenWidth / 2) - (self.windowwidth /2)
        #right-aligning
        aligntop = (screenHeight /2) - (self.windowheight /2)
        #top/bottom aligning
        self.root.geometry('%dx%d+%d+%d' % (self.windowwidth, self.windowheight, alignleft, aligntop))
        
        #text area resizing alongside the window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #textarea control, stretch to window
        self.textarea.grid(sticky = N + E + S + W)

        #formatting the function menu located on top of screen
        self.filemenu.add_command(label="New", command=self.newfile)

        self.filemenu.add_command(label="Open", command=self.openfile)

        self.filemenu.add_command(label="Save", command=self.savefile)

        #small line to separate exit option
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quitapplication)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu.add_command(label="Copy", command=self.copyselection)

        self.editmenu.add_command(label="Paste", command=self.pasteselection)

        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        #add info page for description
        self.helpmenu.add_command(label="About Journal", command=self.showabout)

        self.helpmenu.add_command(label="Internet Search", command=self.searchbar)

        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root.config(menu=self.menubar)

        self.scrollbar.pack(side=RIGHT, fill=Y)

        #allow the scrollbar to follow the text space
        self.scrollbar.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scrollbar.set)
    
    #quits the application
    def quitapplication(self):
        self.root.destroy()
    
    #holds the program description
    def showabout(self):
        showinfo("Journal", "Build strong habits for a better you. Coder: Aleksandr Yeger w/ References")

    #opens dialog for choosing a file to open
    def openfile(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])

        if self.file == "":
            self.file = None

        else:
            self.root.title(os.path.basename(self.file) + " - Journal")
            self.textarea.delete(1.0,END)

            file = open(self.file,"r")

            file.close()

    #creates a blank journal
    def newfile(self):
        self.root.title("Untitled - Journal")
        self.file = None
        self.textarea.delete(1.0,END)

    #saves current work, new file opens dialog
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

    #allows for ctrl+x selected text
    def cutselection(self):
        self.textarea.event_generate("<<Cut>>")

    #allows for ctrl+c selected text
    def copyselection(self):
        self.textarea.event_generate("<<Copy>>")

    #allows for ctrl+v selected text
    def pasteselection(self):
        self.textarea.event_generate("<<Paste>>")



    def searchbar(self):
        root = Tk()
        frame = Frame(root)
        frame.pack()

        def OpenUrl():
            webbrowser.open_new("." + url.get())

        button = Button(frame, text="Search", command=OpenUrl)
        button.pack()

        url = tkinter.Entry(root)
        url.pack()



    #ran to launch the program
    def run(self):
        self.root.mainloop()
    





journal = Journal(width=800,height=600)
journal.run()