"""
Pack: Permite colocar nuestro objetois en la ventana en orden descendente

side: Especifica en qué lado del contenedor se empacará el widget
	-TOP (predeterminado)
	-LEFT
	-RIGHT
	-
fill: X - llenar el contenedor en la dimensión horizontal
	  Y - llenar el contenedor en la dimensión vertical
	  BOTH - llena el contenedor en ambas dimensiones

"""
from tkinter import *

ventana = Tk()

ventana.title("Pack")

btn1 = Button(ventana,text= "Arriba",bg="coral",fg="white")
btn1.pack(side=TOP, fill = X)

btn2 = Button(ventana,text= "Centro",bg="blue",fg="white")
btn2.pack(side=TOP, expand = NO)

btn3 = Button(ventana,text= "Abajo",bg="red",fg="white")
btn3.pack(side=TOP)

ventana.mainloop()


ventana.mainloop()