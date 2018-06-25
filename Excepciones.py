try:
	n=float(input("Introduce un número: "))
	m= 5/n
except ZeroDivisionError:
	print ("No se puede dividir entre cero, prueba otro número")
except TypeError:
	print("No se puede dividir el número por una cadena")
except ValueError:
	print("Debes introducir un número, no una cadena")