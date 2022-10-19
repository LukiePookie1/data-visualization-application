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