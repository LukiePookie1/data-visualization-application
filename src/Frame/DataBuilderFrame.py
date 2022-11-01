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
        self.label.pack(ipadx=0.5, ipady=0.5)
#        self.label.pack(ipadx=1)

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


class DisplayData(tk.Frame):
    def __init__(self, root, CSVData, columns):
        """Initialize a Data Displayer for displaying the data from a specific CSV"""
        super().__init__(root, highlightbackground="blue", highlightthickness=2)
        self.root = root
        self.df = CSVData
        self.columns = columns
        self.numOfGraphs = len(self.columns)        
        self.setupFrameWidget()

    def readData(self):
        """Read the data from the target CSV to df"""
        columns = ["Datetime (UTC)", "Acc magnitude avg", "Eda avg", "Temp avg"]
        self.df = pd.read_csv(self.pathToCSV, usecols=columns)

    def setupFrameWidget(self):
        """Create matplotlib graph, plot points, and display to window"""
        if "Datetime (UTC)" in self.columns:
            self.df["Datetime (UTC)"] = pd.to_datetime(self.df["Datetime (UTC)"])
            self.df["Datetime (UTC)"] = self.df["Datetime (UTC)"].dt.strftime('%H:%M:%S')
            self.df.sort_values(by=["Datetime (UTC)"], inplace=True)
            self.numOfGraphs -= 1

        dateTimeSize = len(self.df["Datetime (UTC)"])

        figure, axs = plt.subplots(1, self.numOfGraphs, sharex=True)
        
        chart_type = FigureCanvasTkAgg(figure, master=self)
        
        if len(self.columns) is 2:
            self.columns.remove("Datetime (UTC)")
            axs.set_xlabel("Time (HH:MM:SS)")
            axs.set_ylabel(self.columns[0])
            axs.xaxis.set_major_locator(plt.MaxNLocator(24))
            axs.tick_params(labelrotation=90)
            axs.grid(color='black', alpha=0.13)
            axs.set_title(self.columns[0])
            axs.margins(x=0.02, y=0.02)            
            axs.plot(self.df["Datetime (UTC)"], self.df[self.columns[0]], lw=2)

        else:
            i = 0;
            for value in self.columns:
                if value != "Datetime (UTC)":
                    axs[i].set_xlabel('Time (HH:MM:SS)')
                    axs[i].set_ylabel(value)
                    axs[i].xaxis.set_major_locator(plt.MaxNLocator(24))
                    axs[i].tick_params(labelrotation=90)
                    axs[i].grid(color='black', alpha=0.13)
                    axs[i].set_title(value)
                    axs[i].margins(x=0.02, y=0.02)
                    axs[i].plot(self.df["Datetime (UTC)"], self.df[value], lw=2)
                    i += 1

        plt.tight_layout()
        chart_type.get_tk_widget().pack(fill=tk.BOTH, expand=True)
