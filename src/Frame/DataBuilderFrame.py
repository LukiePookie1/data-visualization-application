import tkinter as tk
import os
import pandas as pd
from src.Frame.SelectUserAndDateFrame import SelectUserAndDateFrame
from src.Frame.ColumnSelectorFrame import ColumnSelectorFrame

class DataBuilderFrame(tk.Frame):
    """ User interface for configuring dataset and options to load in"""
    def __init__(self, window, pathToDatasets):
        super().__init__(window, highlightbackground="red", highlightthickness=2)

        self.window = window

        self.label = tk.Label(self, text='Data Builder Tab')
        self.label.pack(ipadx=1, ipady=1)

        self.fileSelectorFrame = SelectUserAndDateFrame(self, pathToDatasets)
        self.fileSelectorFrame.pack(anchor=tk.W)

        self.columnSelectorFrame = ColumnSelectorFrame(self)
        self.columnSelectorFrame.pack(anchor=tk.SW)

        self.button = tk.Button(self, text="Create Visual", command=self.CreateVisual)
        self.button.pack(anchor=tk.NE)


    def CreateVisual(self):
        """Button Command Callback To Generate a New Visual Based on User Config"""
        pathToFiles = self.fileSelectorFrame.GetPathToFiles()
        selectedCols = self.columnSelectorFrame.GetChosenColumns()

        if not pathToFiles:
            # Display Error
            return

        if len(selectedCols) == 0:
            # Display Error
            return
        
        # Create Visual Frame
        # Add To Notebook, Maybe Set That Tab as active