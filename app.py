""" 
App.py:
    This is the main Python script to run the application.
    This file should only contain glue code at top level, or temporary development glue code.
"""

from tkinter import *
from src.Window import Window
from src.Utils.Constants import DEFAULTPATHTODATASETS, APPNAME

APPNAME='Digi-Vis'
APPVERSION = '0.0.0.0'
DEFAULTPATHTODATASETS = './datasets'

if __name__ == "__main__":
    window = Window(APPNAME, DEFAULTPATHTODATASETS)
    window.mainloop()
