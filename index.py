# -*- coding:utf-8 -*-

from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title = "Catalogo de productos."

if __name__=='__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()