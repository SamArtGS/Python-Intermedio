import threading
import time

def imprime(numero):
	print("Soy el hilo: ",numero)
	time.sleep(5)
	print("Terminé mi ejecución, soy el hilo: ",numero)
if __name__ == "__main__":
	hilo = threading.Thread(target = imprime, args = (1,))
	hilo2 = threading.Thread(target = imprime, args = (2,))

	hilo.start()
	hilo2.start()

	print("Hola asistentes")

