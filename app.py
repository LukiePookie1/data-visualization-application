""" 
App.py:
    This is the main Python script to run the application.
    This file should only contain glue code at top level, or temporary development glue code.
"""

from tkinter import *
from tkinter import ttk
from src.Window import Window

APPVERSION = '0.0.0.0'

if __name__ == "__main__":
    window = Window()
    window.mainloop()
