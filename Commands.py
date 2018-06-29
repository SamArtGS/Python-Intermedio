from tkinter import *

ventana = Tk()

#iconify = Convierte la ventana en un ícono
#(Sin destruirlo)
# VARIABLES DE CONTROL : CUANDO SE HA MODIFICADO EL OBJETO
#AYUDA A VER CAMBIO DE VALOR.

#

boton = Button(ventana, text = "minimizar",command = ventana.iconify).pack()
Button(ventana, text = "salir",command = quit).pack()
ventana.mainloop()