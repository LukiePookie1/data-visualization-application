import tkinter as tk
from os import path
from src.Utils.DataFrame_Windowed import DataFrame_Windowed
from src.Utils.Constants import SUMMARYFILENAME, METADATAFILENAME
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphManager():
    """Responsible for managing a set of plots"""
    def __init__(self, root, pathToSummaryCsv, chosenCols):
        self.root = root
        self.df_windowed = DataFrame_Windowed(pathToSummaryCsv, chosenCols)
        self.SetupGraphs()

    def SetupGraphs(self):
        """Create matplotlib graph, plot points, and display to window"""
        df = self.df_windowed.GetDataFrame()

        self.numberOfGraphs = len(self.df_windowed.GetSelectedColumns())
        print(f'Number of Graphs Generated: {self.numberOfGraphs}')

        figure, axs = plt.subplots(1, self.numberOfGraphs, sharex=True)

        self.figure = figure
        self.axs = axs

        i = 0
        for column in df.columns:
            print(column)
            if column != 'Datetime (UTC)' and self.numberOfGraphs > 1:
                axs[i].set_xlabel('Time (Hour:Min:Sec)')
                axs[i].set_ylabel(column)
                axs[i].xaxis.set_major_locator(plt.MaxNLocator(24))
                axs[i].tick_params(labelrotation=90)
                axs[i].margins(x=0.02, y=0.02)
                axs[i].grid(color='black', alpha=0.13)
                axs[i].plot(df['Datetime (UTC)'], df[column], lw=2)
                i += 1
            elif column != 'Datetime (UTC)':
                axs.set_xlabel('Time (Hour:Min:Sec)')
                axs.set_ylabel(column)
                axs.xaxis.set_major_locator(plt.MaxNLocator(24))
                axs.tick_params(labelrotation=90)
                axs.margins(x=0.02, y=0.02)
                axs.grid(color='black', alpha=0.13)
                axs.plot(df['Datetime (UTC)'], df[column], lw=2)

        plt.tight_layout()
        canvas = FigureCanvasTkAgg(figure, master=self.root)
        canvas.draw()
        self.canvas = canvas

    def GetCanvas(self):
        return self.canvas


class VisualizerFrame(tk.Frame):
    """Responsible for displaying all plots and synchronizing callbacks in a frame"""

    def __init__(self, notebook, pathToFiles:str, chosenCols:list):
        """Creates a new visualization frame for displaying multiple time series plots"""
        super().__init__(notebook, highlightbackground="green", highlightthickness=2)
        self.summaryCsvPath = path.join(pathToFiles, SUMMARYFILENAME)
        self.metadataCsvPath = path.join(pathToFiles, METADATAFILENAME)
        self.dependentVariables = chosenCols[:]
        self.numOfGraphs = len(self.dependentVariables)

        self.graphManager = GraphManager(self, self.summaryCsvPath, chosenCols)
        self.graphManager.GetCanvas().get_tk_widget().pack(fill=tk.BOTH, expand=True)
