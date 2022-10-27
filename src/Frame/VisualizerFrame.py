import tkinter as tk
import os

from src.Utils.DataFrame_Windowed import DataFrame_Windowed
from src.Utils.Constants import SUMMARYFILENAME, METADATAFILENAME
class VisualizerFrame(tk.Frame):
    """Responsible for displaying all plots and synchronizing callbacks in a frame"""
    def __init__(self, root, pathToFiles, chosenCols):