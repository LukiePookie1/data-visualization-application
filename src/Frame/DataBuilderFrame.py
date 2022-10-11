import tkinter as tk
import os
from functools import partial

class DataBuilderFrame(tk.Frame):
    def __init__(self, pathToDatasets):
        super().__init__(highlightbackground="red", highlightthickness=2)
        self.label = tk.Label(self, text='Data Builder Tab')
        self.label.pack(ipadx=1, ipady=1)

        self.fileSelectorGroup = SelectUserAndDateGroup(self, pathToDatasets)
        self.fileSelectorGroup.pack(anchor=tk.W)


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
        
        self.bind('<Return>', self.debugPrint)

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
        print(self.pathToPatients)
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