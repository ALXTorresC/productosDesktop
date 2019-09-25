#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Tkinter Python 3.7
from tkinter import *

def ventana():
    window = Tk()
    window.title("Tkinter")
    window.geometry('350x200')
    lbl = Label(window, text="Introduce un número")
    lbl.grid(column=0, row=0)
    result = Label(window,text="")
    txt = Entry(window,width=10)
    txt.grid(column=1, row=0)
    result.grid(column=3,row=0)
    txt.focus()
    def mensaje():
        res = txt.get()
        #aquí compruebas que es un número
        res = int(res) if res.isdigit() else 0
        result.configure(text= res)
        txt.delete(0, END)

    btn = Button(window, text="Activa", bg="red",fg="white", command=mensaje)
    btn.grid(column=2, row=0)
    window.mainloop()


def main():
    ventana()

if __name__ == '__main__':
    main()