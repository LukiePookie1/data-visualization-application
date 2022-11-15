import tkinter as tk
from src.Frame.SelectUserAndDateFrame import SelectUserAndDateFrame
from src.Frame.ColumnSelectorFrame import ColumnSelectorFrame
from src.Frame.VisualizerFrame import VisualizerFrame

class DataBuilderFrame(tk.Frame):
    """ User interface for configuring dataset and options to load in"""
    def __init__(self, notebook, pathToDatasets):
        """Creates a frame responsible for handling user input and selection for loading datasets"""
        super().__init__(highlightbackground="red", highlightthickness=2)

        self.notebook = notebook

        self.label = tk.Label(self, text='Data Builder Tab')
        self.label.pack(ipadx=0.5, ipady=0.5)

        self.fileSelectorFrame = SelectUserAndDateFrame(self, pathToDatasets)
        self.fileSelectorFrame.pack(anchor=tk.W)

        self.columnSelectorFrame = ColumnSelectorFrame(self)
        self.columnSelectorFrame.pack(anchor=tk.SW)

        self.button = tk.Button(self, text="Create Visual", command=self.CreateVisual)
        self.button.pack(anchor=tk.NE)


    def CreateVisual(self):
        """Button Command Callback To Generate a New Visual Based on User Config"""
        pathToFiles = self.fileSelectorFrame.GetPathToFiles()
        chosenCols = self.columnSelectorFrame.GetChosenColumns()

        if not pathToFiles:
            # Display Error
            return

        if len(chosenCols) == 0:
            # Display Error
            return

        # Create Visual Frame
        # Add To Notebook, Maybe Set That Tab as active
        visual_frame = VisualizerFrame(self.notebook, pathToFiles, chosenCols)
        visual_frame.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(visual_frame, text='Visual')
