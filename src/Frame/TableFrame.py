import tkinter as tk
from tkinter import ttk
from os import path
from src.Utils.DataFrame_Windowed import DataFrame_Windowed
from src.Utils.Constants import SUMMARYFILENAME

class TableFrame(tk.Frame):
    """Frame responsible for displaying aggregted data in tabular format"""
    def __init__(self, root, pathToFiles:str, chosenCols=['Acc magnitude avg','Eda avg','Temp avg','Movement intensity','Steps count','Rest','On Wrist'], existingDf=None):
        """Create a new aggregation table frame to display. Can use an existing data frame or create new one to aggregate."""
        self.summaryCsvPath = path.join(pathToFiles, SUMMARYFILENAME)
        self.chosenCols = chosenCols
        self.existingDf = existingDf

        super().__init__(root, highlightbackground='blue', highlightthickness=2)
        self.root = root
        self.tree = self.createTable()
        self.patientId = self.fileSelectorFrame.GetPatientId()
        self.dateLabel = str(self.startDate_min) + "-" + str(self.endDate_max)


    def createTable(self):
        """Helper for creating the table with aggregated data"""
        if self.existingDf:
            df_windowed = self.existingDf
        else:
            df_windowed = DataFrame_Windowed(self.summaryCsvPath, colsToKeep=self.chosenCols)

        #Aggregate data, round to 2 decimal places
        summaryStats = df_windowed.Aggregate().round(2)

        #Store column in list to loop over later
        dfCols = summaryStats.columns

        #insert empty space so top left corner is empty, convert column index to list
        dfCols = list(dfCols.insert(0,''))

        #Convert to appropriate format - add column for the count type names in the 0th column
        rowHeaders = ['Count','Mean','STD','Min','25%','50%','75%','Max']
        summaryStats.insert(loc=0, column='type', value=rowHeaders)

        #Convert data to list - easier to import into Tkinter frame
        summaryStats = summaryStats.values.tolist()

        #create tree
        tree = ttk.Treeview(self, columns=dfCols, show='headings')

        #Title for tree
        titleTemp = 'Summary stats for ' + patientId + "(" + dateLabel + ")"
        tree.title(titleTemp)

        #create headers, set column width
        for colHead in dfCols:
            tree.heading(colHead, text=colHead)
            tree.column(column=colHead, width=120)

        #add data
        for obs in summaryStats:
            tree.insert('', tk.END, values=obs)

        #create tree grid, place on root window
        tree.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        return tree
