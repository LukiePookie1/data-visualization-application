import tkinter as tk

"""
DataBuilderFrame:
    Wrapper Class for a Tk Frame.
    This class is responsible for maintaining all data builder widgets and linking all events from each widget to required callbacks.
"""
class DataBuilderFrame(tk.Frame):

    """
    Init:
        Should
    """
    def __init__(self, root):
        super().__init__(root)
        self.pack()
