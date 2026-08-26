import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from pathlib import Path

from Utils.NameFormat import NameFormat
from Data.GeneratedArrays import ArrayGeneration

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
        for i, file in enumerate(folder.glob("*.py")):

            FileName = Formatter.AddSpace(file.name)

            button = tk.Button( self.ButtonFrame, text=FileName)

            button.grid(row=0, column=i, sticky="nsew")

            self.ButtonFrame.grid_columnconfigure(i, weight=1)

            self.buttons.append(button)



    def CreateGraph(self):

        self.figure = plt.figure(figsize=(12,6))
        self.axis = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.window)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        #Generate an array

        self.MainArray = []

        GenerateArray = ArrayGeneration()
        GenerateArray.Randomised(ArrLength=200)
        self.MainArray = GenerateArray.OriginalArray

        self.axis.bar(range(len(self.MainArray)), self.MainArray)

        self.canvas.draw()

    def UpdateGraph(self, UpdatedArray: list):

        self.MainArray = UpdatedArray

        self.axis.clear()

        self.axis.bar(range(len(self.MainArray)), self.MainArray)
        
        self.canvas.draw()



    def mainloop(self):

        self.window.mainloop()

