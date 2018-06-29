import socket
import threading
import time

class HiloCliente(threading.Thread):
	def __init__(self,socketCliente):
		threading.Thread.__init__(self)
		self.socketCliente = socketCliente

	def run(self):
		while True:
			mensaje = self.socketCliente.recv(1024).decode()
			if mensaje == "salir":
				break
			print("Mensaje: "+mensaje+ " desde:" +str(threading.current_thread()))
			#Devuelve el nombre del hilo
			#Después se tiene que cerrar
		self.socketCliente.close()

socketServidor = socket.socket()
socketServidor = bind(("192.168.100.11",9001))

print("Esperando conexiones...")

socketServidor.listen() #Detiene el programa hasta que encuentre una conexión

while True:
	socketCliente, direccion = socketServidor.accept()
	#Devuelve objeto conexión y dirección IP de la cual se conectan
	print("Conectando desde: ",direccion[0])
	hilo = HiloCliente(socketCliente)
	hilo.start()
socketServidor.close()











