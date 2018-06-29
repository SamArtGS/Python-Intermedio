"""
Geometry Manager

-->Grid
Permite colocar objetos por medio de renglones
--* Algunos argumentos --*

row: fila
colum : columnas

Stick: N, S, E, W
columnspan: el widget ocupe más de una columna
rowspan: el widget ocupe másde una fila

"""
from tkinter import *

ventana = Tk()
ventana.title("Grid")
label = Label(ventana, text = "Soy un label")
label.grid(row=1,column =1)

label2=Label(ventana, text = "Grid en otra posicion")
label2.grid(row=2,column=2)

label3 = Label(ventana, text = "Se ignoran las columnas vacías")
label3.grid(row = 30, column= 50)
ventana.mainloop()
