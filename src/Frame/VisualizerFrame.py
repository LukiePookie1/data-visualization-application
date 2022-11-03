import tkinter as tk
from os import path
from src.Utils.DataFrame_Windowed import DataFrame_Windowed
from src.Utils.Constants import SUMMARYFILENAME, METADATAFILENAME
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates

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
        print('here 2')

        self.numberOfGraphs = len(df) - 1

        figure, axs = plt.subplots(1, self.numberOfGraphs, sharex=True)

        self.figure = figure
        self.axs = axs
        
        canvas = FigureCanvasTkAgg(figure, master=self)
        self.canvas_tk = canvas

        i = 0
        for column in df.columns:
            if column != 'Datetime (UTC)':
                axs[i].set_xlabel('Datetime (UTC)')
                axs[i].set_ylabel(column)
                axs[i].xaxis.set_major_locator(plt.MaxNLocator(24))
                axs[i].tick_params(labelrotation=90)
                axs[i].margins(x=0.02, y=0.02)
                axs[i].grid(color='black', alpha=0.13)
                axs[i].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
                axs[i].set_title(column)
                axs[i].plot(df['Datetime (UTC)'].head(), df[column].head(), lw=2)
                i += 1

        plt.tight_layout()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

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
        self.graphManagerFrame.pack()
