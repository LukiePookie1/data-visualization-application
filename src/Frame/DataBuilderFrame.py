import tkinter as tk
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataBuilderFrame(tk.Frame):
    """ User Interface for configuring dataset and options to load in"""
    def __init__(self, pathToDatasets):
        super().__init__(highlightbackground="red", highlightthickness=2)
        self.label = tk.Label(self, text='Data Builder Tab')
        self.label.pack(ipadx=1, ipady=1)

        self.fileSelectorGroup = SelectUserAndDateGroup(self, pathToDatasets)
        self.fileSelectorGroup.pack(anchor=tk.W)

        self.button = tk.Button(self, text="Save", command=self.chooseCols)
        self.button.pack(ipadx=1, ipady=1)


    def chooseCols(self):
        self.pathToCSV = os.path.join(self.fileSelectorGroup.GetPathToFiles(), 'summary.csv')
        self.fileSelectorGroup.destroy()
        self.button.destroy()
        self.colChooseGroup = ChooseColumns(self, self.pathToCSV)
        self.colChooseGroup.pack(anchor=tk.W)

        self.button = tk.Button(self, text="Save", command=self.display)
        self.button.pack(ipadx=1, ipady=1)

    def display(self):
        self.CSVData = self.colChooseGroup.getCSVData()
        self.chosenCols = self.colChooseGroup.getChoseCols()
        self.colChooseGroup.destroy()
        self.button.destroy()
        self.dataViewGroup = DisplayData(self, self.CSVData, self.chosenCols)
        self.dataViewGroup.pack(anchor=tk.W)

class SelectUserAndDateGroup(tk.Frame):
    def __init__(self, root, pathToDatasets):
        """Initialize a Patient and Date Selector for selecting specific pair of CSVs to load"""
        if not os.path.isdir(pathToDatasets):
            raise Exception('Path to Datasets: ' + pathToDatasets + ' does not exist or is not a directory.')

        super().__init__(root, highlightbackground="green", highlightthickness=2)
        self.root = root
        self.pathToDatasets = pathToDatasets
        self.pathToPatients = None
        self.pathToFiles = None

        self.dateList = []
        self.dateListVar = tk.StringVar(value=self.dateList)
        self.UpdateDateOptions()
        self.dateListbox = tk.Listbox(self, selectmode=tk.SINGLE, listvariable=self.dateListVar)
        self.dateListbox.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)
        self.dateListbox.bind('<<ListboxSelect>>', self.OnDateSelected)

        self.patientList = []
        self.patientListVar = tk.StringVar(value=self.patientList)
        self.patientListbox = tk.Listbox(self, selectmode=tk.SINGLE, listvariable=self.patientListVar)
        self.patientListbox.pack(side=tk.RIGHT, expand=tk.NO, fill=tk.BOTH)
        self.patientListbox.bind('<<ListboxSelect>>', self.OnPatientSelected)
        # self.patientListbox.bind('<Return>', self.debugPrint)


    def UpdateDateOptions(self):
        """ Update date list and listbox of dates"""
        self.dateList = []
        for i in os.listdir(self.pathToDatasets):
            self.dateList.append(i)

        self.dateList.sort()
        self.dateListVar.set(self.dateList)


    def UpdatePatientOptions(self):
        """ Update patient list and listbox of patients"""
        self.patientList = []
        for i in os.listdir(self.pathToPatients):
            self.patientList.append(i)

        self.patientList.sort()
        self.patientListVar.set(self.patientList)


    def OnDateSelected(self, evt=None):
        """Callback for user selection of date. Updates Patient list"""
        try:
            selected_index = self.dateListbox.curselection()[0]
        except IndexError:
            return

        self.pathToPatients = os.path.join(self.pathToDatasets, self.dateListbox.get(selected_index))
        #print(self.pathToPatients)
        self.UpdatePatientOptions()


    def OnPatientSelected(self, evt=None):
        """Callback for user selection of patient id. Updates file path to patient files"""
        try:
            selected_index = self.patientListbox.curselection()[0]
        except IndexError:
            return

        self.pathToFiles = os.path.join(self.pathToPatients, self.patientListbox.get(selected_index))


    def GetPathToFiles(self):
        """Get a copy of the path to patient data files based on current user selections"""
        if self.pathToFiles:
            return str(self.pathToFiles)
        else:
            print('No path available from data builder panel.')
            return None


    def debugPrint(self, evt=None):
        print('Debug: ' + self.pathToFiles)

class ChooseColumns(tk.Frame):
    def __init__(self, root, pathToCSV):
        if not os.path.isfile(pathToCSV):
            raise Exception('Path to CSV: ' + pathToCSV + ' does not exist or is not a file.')

        super().__init__(root, highlightbackground="pink", highlightthickness=2)
        self.root = root
        self.pathToCSV = pathToCSV
        self.df = None
        self.unchosenColumns = []
        self.chosenColumns = []
        self.getAllCols()
        self.unchoseColVar = tk.StringVar(value=self.unchosenColumns)
        self.choseColVar = tk.StringVar(value=self.chosenColumns)

        self.unchoseColListbox = tk.Listbox(self, selectmode=tk.SINGLE, listvariable=self.unchoseColVar)
        self.unchoseColListbox.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)
        self.choseColListbox = tk.Listbox(self, selectmode=tk.SINGLE, listvariable=self.choseColVar)
        self.choseColListbox.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)

        self.addColButton = tk.Button(self, text="Add Column", command=self.addCol)
        self.addColButton.pack()
        self.removeColButton = tk.Button(self, text="Remove Column", command=self.removeCol)
        self.removeColButton.pack()

    def getAllCols(self):
        self.df = pd.read_csv(self.pathToCSV)
        for col in self.df.columns:
            self.unchosenColumns.append(col)
        self.unchosenColumns.sort()
        #print('Debug: ', self.unchosenColumns)

    def addCol(self):
        try:
            selected_index = self.unchoseColListbox.curselection()[0]
        except IndexError:
            return

        col = self.unchoseColListbox.get(selected_index)
        self.chosenColumns.append(col)
        self.unchosenColumns.remove(col)
        self.updateWindow()

    def removeCol(self):
        try:
            selected_index = self.choseColListbox.curselection()[0]
        except IndexError:
            return

        col = self.choseColListbox.get(selected_index)
        self.unchosenColumns.append(col)
        self.chosenColumns.remove(col)
        self.updateWindow()

    def updateWindow(self):
        self.chosenColumns.sort()
        self.unchosenColumns.sort()

        self.unchoseColListbox.destroy()
        self.choseColListbox.destroy()
        self.addColButton.destroy()
        self.removeColButton.destroy()

        self.unchoseColVar = tk.StringVar(value=self.unchosenColumns)
        self.choseColVar = tk.StringVar(value=self.chosenColumns)

        self.unchoseColListbox = tk.Listbox(self, selectmode=tk.SINGLE, listvariable=self.unchoseColVar)
        self.unchoseColListbox.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)
        self.choseColListbox = tk.Listbox(self, selectmode=tk.SINGLE, listvariable=self.choseColVar)
        self.choseColListbox.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)

        self.addColButton = tk.Button(self, text="Add Column", command=self.addCol)
        self.addColButton.pack()
        self.removeColButton = tk.Button(self, text="Remove Column", command=self.removeCol)
        self.removeColButton.pack()
    
    def getCSVData(self):
        return self.df

    def getChoseCols(self):
        return self.chosenColumns

class DisplayData(tk.Frame):
    def __init__(self, root, CSVData, columns):
        """Initialize a Data Displayer for displaying the data from a specific CSV"""
        super().__init__(root, highlightbackground="blue", highlightthickness=2)
        self.root = root
        self.df = CSVData
        self.columns = columns
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