import tkinter as tk

"""
DataBuilderFrame:
    Extended Class for a Tk Frame.
    This class is responsible for maintaining all data builder widgets and linking all events from each widget to required callbacks.
    This Class has:
    - a dropdown menu, listing patient id's which will determine which set to import
    - a multi-select menu for listing the different metrics from the CSVs to load
    - a radio button for selecting UTC time or Local time
    - a button which will trigger the creation of a new Notebook tab with a DataVisualFrame
"""
class DataBuilderFrame(tk.Frame):

    """
    Init:
        Should
    """
    def __init__(self, root):
        super().__init__(root)
