from tkinter import Tk, Label, Button


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("The GUI Title.")

        self.label = Label(master, text="This is the Label!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet Button.", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close Button.", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()