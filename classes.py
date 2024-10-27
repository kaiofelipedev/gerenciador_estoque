from tkinter import *

class App():
    def __init__(self):
        self.window = Tk()
        self.settings()
        mainloop()

    def settings(self):
        self.window.title("GereFácil App")
        self.window.geometry("480x400")
        self.window.configure(background="#262626")
        self.window.minsize(width= 480, height= 400)
