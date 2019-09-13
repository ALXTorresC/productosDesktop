# -*- coding:utf-8 -*-

from tkinter import ttk
from tkinter import *

import sqlite3


class Product:

    'Base de datos: database.db'
    db_name = 'database.db'

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(query, parameters)
            conn.commit()
        return resultado

    def get_products(self):
        query = 'SELECT * FROM product ORDER BY Nombre DESC'
        filas_db = self.run_query(query)
        print(filas_db)

    def __init__(self, window):
        self.wind = window
        self.wind.title = "Catalogo de productos."

        # Creando un contenedor para agregar elementos.
        frame = LabelFrame(self.wind, text = "Registrar un nuevo producto")
        frame.grid(row=0, column = 0, columnspan = 3, padx=20, pady=20)
    
        # Input
        Label(frame, text="Nombre:").grid(row=1, column=0, pady=10, padx=5)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1,padx=5)

        # Price input
        Label(frame, text="Precio:").grid(row=2, column=0, pady=5, padx=5)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1, padx=5)

        # Botón del formulario
        ttk.Button(frame, text="Guardar producto").grid(row=3, pady=5, padx=5, columnspan=2, sticky = W + E)

        # Arbol de vista
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid( row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text="Nombre", anchor = CENTER)
        self.tree.heading('#1', text="Precio", anchor = CENTER)

        self.get_products()

if __name__=='__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()