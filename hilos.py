#Hilos

#Los hilos en Python se implementan con la clase Thread

import threading

class Hilo(threading.Thread):
	def __init__(self,numero):
		threading.Thread.__init__(self)
		self.numero=numero
		#Hilo: multiples ejecuciones en el mismo programa
		#Proceso: Recuersos para cada proceso
		#Hilo: Comparte recursos para cada hilo
	#Método run - Especifica las tareas que va a realizar el hilo.
	#Este método proviene de Thread

	def run(self):
		print("Hilo no: ",self.numero)
		print("Terminé mi ejecución, soy el hilo número: ",self.numero)
		time.sleep(5)
if __name__ == "__main__":
	#Si tenemos una clase lo que se debe realizar es instanciar al objeto
	hilo1 = Hilo(1)
	hilo2 = Hilo(2)
	hilo1.start()
	hilo2.start()
	print("Estoy dentro del hilo principal")
