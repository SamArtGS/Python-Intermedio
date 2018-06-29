import socket

socketCliente = socket.socket()

socketCliente.connect(("192.168.3.13",5555))

while True:
	mensaje = input("Ingrese un mensaje: ")
	socketCliente.send(mensaje.encode())
	if mensaje == "salir":
		break
socketCliente.close()