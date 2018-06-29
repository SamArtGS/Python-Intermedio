"""
Variables de control 

-BooleanVar
-DoubleVar
-IntVar
-StringVar

"""

from tkinter import *

ventana = Tk()
var = StringVar()
label = Label(ventana)

def seleccion():
	select = "Tu selección fue: "+(var.get())
	label.config(text=select)

r1 = RadioButton(ventana, text = "opción 1",variable=var,value = "1",command = seleccion)
r1.pack()
r2 = RadioButton(ventana, text = "opción 2",variable=var,value = "2",command = seleccion)
r2.pack()
r3 = RadioButton(ventana, text = "opción 3",variable=var,value = "3",command = seleccion)
r3.pack()

label.pack()
ventana.mainloop()

