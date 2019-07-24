from tkinter import *
import tkinter, webbrowser

root = Tk()
frame = Frame(root)
frame.pack()

def OpenUrl():
    webbrowser.open_new("." + url.get())

url = tkinter.Entry(root)
url.pack()

button = Button(frame, text="Search", command=OpenUrl)
button.pack()
root.mainloop()
