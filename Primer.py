print("Hola mundo")

#x = 2 * var* 4
"""
l = [1,2]
l.pop()
l.pop()
l.pop()"""
# Las excepciones son errores en tiempo de ejecucion
# try - except
while True:
	try:
		n = float(input("Introduce un numero: "))
		m = 5
		print("{0}/{1} = {2}".format(n,m,n/m))
	except:
		print("Ha ocurrido un error. Introduce bien el numero")
	else: #En caso de que no haya excepcion
		print("Todo ha funcionado correctamente")
		break
	finally: #siempre se ejecuta, si hay excepcion o no
		print("Fin de la iteracion")
