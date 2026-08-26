import tkinter as tk
from pathlib import Path

from Utils.NameFormat import NameFormat

class SortGUI:

    #init function
    def __init__(self):

        #Create Window
        self.window =  tk.Tk()

        self.window.title("Sorting Visualizer")
        self.window.geometry("1200x800")

        #Button Setup

        self.ButtonFrame = tk.Frame(self.window)
        self.ButtonFrame.pack(side="top", fill="x")

        Formatter = NameFormat()

        self.buttons = []

        folder = Path(__file__).parent.parent/"SortFunctions"
        for file in folder.glob("*.py"):

            FileName = Formatter.AddSpace(file.name)

            button = tk.Button( self.ButtonFrame, text=FileName)

            button.pack(side="left", padx=5)

            self.buttons.append(button)



    def mainloop(self):

        self.window.mainloop()

