try:
	n=float(input("Introduce un número: "))
	m= 5/n
except ZeroDivisionError: #Excepcion de división entre 0
	print ("No se puede dividir entre cero, prueba otro número")
except TypeError: #Excepción cuando se haya insertado un String
	print("No se puede dividir el número por una cadena")
except ValueError: #Excepción 
	print("Debes introducir un número, no una cadena")