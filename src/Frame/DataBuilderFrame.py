import tkinter as tk
from src.Frame.SelectUserAndDateFrame import SelectUserAndDateFrame
from src.Frame.ColumnSelectorFrame import ColumnSelectorFrame
from src.Frame.VisualizerFrame import VisualizerFrame
from src.Frame.TableFrame import TableFrame

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

        self.createVisualButton = tk.Button(self, text="Create Visual", command=self.CreateVisual)
        self.createVisualButton.pack(anchor=tk.NE)

        self.createTableButton = tk.Button(self, text="Create Summary", command=self.CreateSummary)
        self.createTableButton.pack(anchor=tk.E)

        self.numberOfVisuals = 0
        self.numberOfTables = 0


    def CreateSummary(self):
        pathToFiles = self.fileSelectorFrame.GetPathToFiles()
        chosenCols = self.columnSelectorFrame.GetChosenColumns()

        table_frame = TableFrame(self.notebook, pathToFiles, chosenCols)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        self.numberOfTables += 1
        self.notebook.add(table_frame, text=f'Table {self.numberOfTables}')


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

        self.numberOfVisuals += 1
        self.notebook.add(visual_frame, text=f'Visual {self.numberOfVisuals}')
        
