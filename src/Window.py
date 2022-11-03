import tkinter as tk
from tkinter.ttk import Notebook
from src.Frame.DataBuilderFrame import DataBuilderFrame

class Window(tk.Tk):
    def __init__(self, appname, pathToDatasets):
        super().__init__()
        self.title(appname)
        self.geometry('1200x900')

        self.notebook = Notebook(self)

        data_builder_tab = DataBuilderFrame(self.notebook, pathToDatasets)
        self.notebook.add(data_builder_tab, text='Builder')
        self.notebook.pack(fill=tk.BOTH, expand=1)
