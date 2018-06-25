def miFuncion(algo=None): #Condición en el caso que los parámetros sean nulos
	try:
		if algo == None:
			print ("Invoca al error")
			raise ValueError #Forzar la ejecución del error
	except ValueError:
		print("Debes pasarle un parámetro")

class miExcepcion(Exception):
	def _init_(self, mensaje):
		self.mensaje = mensaje

def funcion (algo=None):
	if algo == None:
		raise miExcepcion("Esta es mi excepción")
funcion()