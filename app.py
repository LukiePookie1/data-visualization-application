""" 
App.py:
    This is the main Python script to run the application.
    This file should only contain glue code at top level, or temporary development glue code.
"""

from tkinter import *
from tkinter import ttk

APPNAME='DigiVis'

root = Tk(className=APPNAME)
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()