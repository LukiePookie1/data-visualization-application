import tkinter as tk

APPNAME='Digi-Vis'

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text='Hello World', padx=5, pady=5)
        self.label.pack()
        self.geometry('800x600')
        self.title(APPNAME)

