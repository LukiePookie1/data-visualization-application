import tkinter as tk
from os import path
from src.Utils.DataFrame_Windowed import DataFrame_Windowed
from src.Utils.Constants import SUMMARYFILENAME, METADATAFILENAME
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphManagerFrame(tk.Frame):
    """Responsible for managing a set of plots"""
    def __init__(self, root, pathToSummaryCsv, chosenCols):
        super().__init__(root, highlightbackground='orange', highlightthickness=2)
        self.root = root
        self.df_windowed = DataFrame_Windowed(pathToSummaryCsv, chosenCols)
        self.SetupGraphs()

    def SetupGraphs(self):
        """Create matplotlib graph, plot points, and display to window"""
        print('here 1')
        df = self.df_windowed.GetDataFrame()

        self.numberOfGraphs = len(df) - 1

        print('here 2')
        figure, axs = plt.subplots(1, self.numberOfGraphs, sharex=True)
        print('here 3')

        self.figure = figure
        self.axs = axs

        i = 0
        for column in df.columns:
            print(column)
            if column != 'Datetime (UTC)':
                axs[i].set_xlabel('Time (Hour:Min:Sec)')
                axs[i].set_ylabel(column)
                axs[i].xaxis.set_major_locator(plt.MaxNLocator(24))
                axs[i].tick_params(labelrotation=90)
                axs[i].margins(x=0.02, y=0.02)
                axs[i].grid(color='black', alpha=0.13)
                axs[i].plot(df['Datetime (UTC)'], df[column], lw=2)
                i += 1

        print('here 4')
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(figure, master=self)
        canvas.draw()
        print('here 5')
        canvas.get_tk_widget().pack(anchor=tk.W, fill=tk.BOTH, expand=True)
        print('here 6')
        self.canvas_tk = canvas

class VisualizerFrame(tk.Frame):
    """Responsible for displaying all plots and synchronizing callbacks in a frame"""

    def __init__(self, root, pathToFiles:str, chosenCols:list):
        """Creates a new visualization frame for displaying multiple time series plots"""

        super().__init__(root, highlightbackground="green", highlightthickness=2)
        self.root = root
        self.summaryCsvPath = path.join(pathToFiles, SUMMARYFILENAME)
        self.metadataCsvPath = path.join(pathToFiles, METADATAFILENAME)
        self.dependentVariables = chosenCols[:]
        self.numOfGraphs = len(self.dependentVariables)

        self.graphManagerFrame = GraphManagerFrame(self, self.summaryCsvPath, chosenCols)
        self.graphManagerFrame.pack(fill=tk.BOTH, expand=True)
