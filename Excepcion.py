#try:
#	f=open("archivo.txt","r")
#	datos=f.readlines()
#except:
#	print("Error al abrir el fichero")
#finally:
#	f.close()
#
with open("archivo.txt","r") as f:
	contenido = f.read() #PAra que se ejecuten automáticamente sentencias, al terminar esa sentencia pasará automáticamente algo
class closing(object):
	def __init__(self,obj):
		self.obj=obj
	def __enter__(self):
		return self.obj
	def __exit__(self,*args):
		self.obj.close()
	def write(self,cadena):
		self.obj.write(cadena)
with closing(open("archivo.txt","w")) as f: #Ejecutar algo, ponerle un alias
	f.write("Un nuevo archivo")

class test(object): 
	def __init__(self,n): #Son métodos mágicas en Python.
		print("en init...")
		self.n=n
	def __enter__(self):	##Método mágico con 2 guiones bajos
		print("Entrando...")
		return self
	def __exit__(self,*args): #Método mágico 
		print("Saliendo")
	def metodo(self):
		print("n vale: {0}".format(self.n))
with test(8) as wt:
	wt.metodo()
