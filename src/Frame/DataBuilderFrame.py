import tkinter as tk

from matplotlib.pyplot import grid

class DataBuilderFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text='Data Builder Tab')
        self.label.pack(ipadx=1, ipady=1)