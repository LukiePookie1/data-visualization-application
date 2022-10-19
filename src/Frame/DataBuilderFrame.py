import tkinter as tk
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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

#     def chooseCols(self):
#         self.pathToCSV = os.path.join(self.fileSelectorFrame.GetPathToFiles(), 'summary.csv')
#         self.fileSelectorFrame.destroy()
#         self.button.destroy()
#         self.colChooseGroup = ChooseColumns(self, self.pathToCSV)
#         self.colChooseGroup.pack(anchor=tk.W)

#         self.button = tk.Button(self, text="Save", command=self.display)
#         self.button.pack(ipadx=1, ipady=1)

#     def display(self):
#         self.CSVData = self.colChooseGroup.getCSVData()
#         self.chosenCols = self.colChooseGroup.getChoseCols()
#         self.colChooseGroup.destroy()
#         self.button.destroy()
#         self.dataViewGroup = DisplayData(self, self.CSVData, self.chosenCols)
#         self.dataViewGroup.pack(anchor=tk.W)


# class DisplayData(tk.Frame):
#     def __init__(self, root, CSVData, columns):
#         """Initialize a Data Displayer for displaying the data from a specific CSV"""
#         super().__init__(root, highlightbackground="blue", highlightthickness=2)
#         self.root = root
#         self.df = CSVData
#         self.columns = columns
#         self.setupFrameWidget()


#     def readData(self):
#         """Read the data from the target CSV to df"""
#         columns = ["Datetime (UTC)", "Acc magnitude avg", "Eda avg", "Temp avg"]
#         self.df = pd.read_csv(self.pathToCSV, usecols=columns)


#     def setupFrameWidget(self):
#         """Create matplotlib graph, plot points, and display to window"""
#         if "Datetime (UTC)" in self.columns:
#             self.df["Datetime (UTC)"] = pd.to_datetime(self.df["Datetime (UTC)"])
#             self.df["Datetime (UTC)"] = self.df["Datetime (UTC)"].dt.strftime('%H:%M:%S')
#         figure = plt.Figure(figsize=(15,10), dpi=100)
#         ax = figure.add_subplot(111)
#         chart_type = FigureCanvasTkAgg(figure, self)
#         chart_type.get_tk_widget().pack()
#         if "Datetime (UTC)" in self.columns:
#             self.df[self.columns].set_index('Datetime (UTC)').plot(rot=0, kind='line', legend=True, ax=ax)
#             ax.set_xlabel('Time (HH:MM:SS)')
#         else:
#             self.df[self.columns].plot(rot=0, kind='line', legend=True, ax=ax)
#             ax.set_xlabel('Row Number')
#         ax.set_title('Data Line Chart')
#         ax.set_ylabel('Value')