import socket
socketCliente = socket.socket()

socketCliente.connect(("193.168.3.20",9003))

while True:
	mensaje = input("Ingrese un mensaje: ")
	socketCliente.send(mensaje.encode())
	if mensaje == "salir":
		break
	mensaje1 = socketCliente.recv(1024).decode()
	print("Mensaje: " +mensaje1)
socketCliente.close()
