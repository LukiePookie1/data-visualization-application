import tkinter as tk
from tkinter import ttk
from os import path
from src.Utils.DataFrame_Windowed import DataFrame_Windowed
from src.Utils.Constants import SUMMARYFILENAME, METADATAFILENAME



class TableFrame(tk.Frame):

    #Init with default to all numeric columns
    def __init__(self,root, pathToFiles:str, chosenCols=['Acc magnitude avg','Eda avg','Temp avg','Movement intensity','Steps count','Rest','On Wrist']):

        #Path to chosen summary csv
        self.summaryCsvPath = path.join(pathToFiles, SUMMARYFILENAME)

        #initialize tree
        super().__init__(root)
        self.root = root
        self.tree = self.createTable()



    def createTable(self):

        #read data in
        data = DataFrame_Windowed(summaryCsvPath,colsToKeep=chosenCols)


        #Aggregate data, round to 2 decimal places
        summaryStats = data.Aggregate().round(2)

        #Store column in list to loop over later
        dfCols = summaryStats.columns

        #Convert to appropriate format - add column for the count type names in the 0th column
        rowHeaders = ['Count','Mean','STD','Min','25%','50%','75%','Max']
        summaryStats.insert(loc= 0, column = 'type', value=rowHeaders)

        #Convert data to list - easier to import into Tkinter frame
        summaryStats = summaryStats.values.tolist()

        #insert empty space so top left corner is empty, convert column index to list
        dfCols = list(dfCols.insert(0,''))

        #create tree
        tree = ttk.Treeview(self, columns = dfCols, show='headings')

        #create headers, set column width
        for colHead in dfCols:
            tree.heading(colHead,text=colHead)
            tree.column(column = colHead,width=120)

        #add data
        for obs in summaryStats:
            tree.insert('', tk.END, values=obs)

        #create tree grid, place on root window
        tree.grid(row=0,column=0,sticky='nsew')

        return tree
