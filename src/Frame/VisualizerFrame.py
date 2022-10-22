import tkinter as tk
import os

from src.Utils.DataFrame_Windowed import DataFrame_Windowed
from src.Utils.Constants import SUMMARYFILENAME, METADATAFILENAME
class VisualizerFrame(tk.Frame):
    """Responsible for displaying all plots and synchronizing callbacks in a frame"""
    def __init__(self, root, pathToFiles, chosenCols):
        super().__init__(root, highlightbackground='red', highlightthickness=2)
        self.root = root
        self.summaryCsvPath = os.path.join(pathToFiles, SUMMARYFILENAME)
        self.metadataCsvPath = os.path.join(pathToFiles, METADATAFILENAME)


    def setupFrameWidget(self):
        """Create matplotlib graph, plot points, and display to window"""
        if "Datetime (UTC)" in self.columns:
            self.df["Datetime (UTC)"] = pd.to_datetime(self.df["Datetime (UTC)"])
            self.df["Datetime (UTC)"] = self.df["Datetime (UTC)"].dt.strftime('%H:%M:%S')
        figure = plt.Figure(figsize=(15,10), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, self)
        chart_type.get_tk_widget().pack()
        if "Datetime (UTC)" in self.columns:
            self.df[self.columns].set_index('Datetime (UTC)').plot(rot=0, kind='line', legend=True, ax=ax)
            ax.set_xlabel('Time (HH:MM:SS)')
        else:
            self.df[self.columns].plot(rot=0, kind='line', legend=True, ax=ax)
            ax.set_xlabel('Row Number')
        ax.set_title('Data Line Chart')
        ax.set_ylabel('Value')