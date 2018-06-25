import os

personas = {}

while True:
	print("----- AGENDA -----")
	print("1.Capturar datos del contacto")
	print("2. Ver datos")
	print("3. Ver todos los contactos")
	print("4. Eliminar contacto")
	print("5. Salir")

	opcion = int(input("\nElige una opción: "))

	if opcion == 1:
		nombre = input("Escribe el nombre de la persona: ")
		apellido = input("Escribe el apellido de la persona: ")
		telefono = input("Ingresa el teléfono de la persona: ")

		personas[nombre]=apellido

		f=open(nombre+apellido+".txt","w")

		f.write("Nombre: "+nombre+"\nApellido: "+apellido+"\nTeléfono: "+telefono)

		f.close()
		os.system("clear")
		
	elif opcion == 2:
		try:
			nombre = input("Escribe el nombre de la persona: ")
			apellido = input("Escribe el apellido de la persona: ")
			f= open(nombre+apellido+".txt","r")
			print("Datos: \n",f.read())
			f.close()
			os.system("clear")
		except FileNotFoundError:
			print("No se encontrarion los datos de la persona especificada")
			os.system("clear")
	elif opcion == 3:
		print("Personas:\n")
		for clave,valor in personas.items(): # método que devuelve una lista de tuplas
			.
			.
			print(clave + " " + valor)
		os.system("clear")
	elif opcion == 4:
		nombre = input("Ingresa el nombre de la persona que deseas eliminar: ")
		apellido = input("Escribe el apellido de la persona: ")
		del personas[nombre]
		os.remove(nombre+apellido+".txt")
		os.system("clear")
	elif opcion == 5:
		print("Hasta luego")
		break
	else: 
		print("Ingrese una opción válida")
		os.system("clear")