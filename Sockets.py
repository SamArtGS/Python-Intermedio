#Sockets

# Es la forma de comunicar programas/equipos bajo la misma red

#Se resuelve mediante Sockets
#Para crear un socket se necesita una IP y un Port

# Siempre y cuando se encuentre bajo la misma red

import socket
socketServidor = socket.socket()



socketServidor.bind(("192.168.3.20",9002))
#(ip, puerto libre (checar protocolo))
print("Esperando conexiones...")
socketServidor.listen(1) #Detiene el programa hasta que alguien intenta conectarse

socketCliente,direccion = socketServidor.accept()
#accept devuelve tupla (conn, ip)

print("Conectado desde: ",direccion[0])

while True:
	mensaje = socketCliente.recv(1024).decode()
	if mensaje == "salir":
		break
	print("Mensaje: " +mensaje)

socketCliente.close()