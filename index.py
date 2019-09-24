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
        # Limpiando la tabla de datos
        records =self.tree.get_children()
        for element in records:
            self.tree.delete(element)
            print(element)
        # Consultando los datos
        query = 'SELECT * FROM product ORDER BY Nombre DESC'
        filas_db = self.run_query(query)
        for fila in filas_db:
            self.tree.insert("", 0, text=fila[1], value=fila[2])
            print(fila)

    def campos_no_vacios(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    # Añadir un producto
    def add_product(self):
        if self.campos_no_vacios():
            query = "INSERT INTO product VALUES(NULL, ?, ?)"
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['fg'] = 'dark green'
            self.message['text'] = "'{}' ha sido añadido exitosamente.".format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['fg'] = 'red'
            self.message['text'] = "El nombre y el precio son requeridos."
        self.get_products()

    # Eliminar un producto.
    def delete_product(self):
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['fg'] = 'red'
            self.message['text'] = 'Debe seleccionar un ítem.'
            return
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE Nombre = ?'
        self.run_query(query, (name, ))
        self.message['fg'] = 'dark green'
        self.message['text'] = "Ítem '{}' se ha eliminado correctamente".format(name)
        self.get_products()

    # Actualizar un producto
    def update_product(self):
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['fg'] = 'red'
            self.message['text'] = 'Debe seleccionar un ítem.'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]

        # Ventana de edición
        self.edit_window = Toplevel()
        self.edit_window.title('Editar producto')

        # Nombre anterior
        Label(self.edit_window, text='Nombre anterior ').grid(row = 0, column = 1)
        Entry(self.edit_window, textvariable=StringVar(self.edit_window, value = name), state ='readonly').grid(row=0, column=2)

        # Nuevo nombre
        Label(self.edit_window, text='Nombre nuevo ').grid(row=1, column=1)
        new_name = Entry(self.edit_window)
        new_name.grid(row=1, column=2)

        # Precio anterior
        Label(self.edit_window, text='Precio anterior ').grid(row=2, column=1)
        Entry(self.edit_window, textvariable=StringVar(self.edit_window, value=old_price), state='readonly').grid(row=2, column=2)

        # New price
        Label(self.edit_window, text="Precio nuevo ").grid(row=3, column=1)
        new_price = Entry(self.edit_window)
        new_price.grid(row = 3, column = 2)

        # Botón de confirmación
        ttk.Button(self.edit_window, text="Editar registro", command = lambda:self.edit_records(new_name.get(),name, new_price.get(), old_price)).grid(row=4,column=1,columnspan=2,pady=5, sticky=W+E)

    def edit_records(self,new_name, old_name, new_price, old_price):

        query = 'UPDATE product SET Nombre = ?, Precio = ? WHERE Nombre = ? AND Precio = ?'
        parameters = (new_name, new_price, old_name, old_price)
        self.run_query(query, parameters)
        self.edit_window.destroy()
        self.message['fg']='dark green'
        self.message['text']="'{}' ha sido actualizado exitosamente.".format(new_name)
        self.get_products()

    def __init__(self, window):
        self.wind = window
        self.wind.title("Catalogo de productos.")

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
        ttk.Button(frame, text="Guardar producto",command=self.add_product).grid(row=3, pady=5, padx=5, columnspan=2, sticky = W + E)

        # Mensajes de salida
        self.message = Label(text='')
        self.message.grid(row = 3, column=0, columnspan=2, sticky=W+E)

        # Arbol de vista
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid( row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text="Nombre", anchor = CENTER)
        self.tree.heading('#1', text="Precio", anchor = CENTER)

        # Botones eliminar y editar.
        ttk.Button(text='Eliminar', command = self.delete_product).grid(row=5, column=0, sticky = W + E)
        ttk.Button(text='Editar', command = self.update_product).grid(row=5, column=1,sticky= W + E)

        self.get_products()

if __name__=='__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()