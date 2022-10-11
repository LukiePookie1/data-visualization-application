import tkinter as tk
from tkinter.ttk import Notebook
from src.Frame.DataBuilderFrame import DataBuilderFrame

APPNAME='Digi-Vis'

class Window(tk.Tk):
    def __init__(self, pathToDatasets):
        super().__init__()
        self.geometry('800x600')
        self.title(APPNAME)

        self.notebook = Notebook(self)

        data_builder_tab = DataBuilderFrame(pathToDatasets)
        self.notebook.add(data_builder_tab, text='Builder')
        self.notebook.pack(fill=tk.BOTH, expand=1)

