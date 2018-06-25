#Abrir archivo
#open(ruta, modo de abirlo)

#Modos de apertura
#r->read, lectura, el archivo debe existir 

#w->write, escritura, si el archivo no existe lo crea, si existe lo sobreescribe

#a->append, añadir, agrega datos al final del archivo

# + -> r y w. 

#Abrir un archivo
#Por dafault en modo lectura

#objeto = open("archivo.txt")
#Se abre el archivo en modo escritura

#objeto = open("archivo.txt","w")

#Cerrar archivo

#objeto.close()
#objeto.close()
#Leer

#read-> lee todo el archivo
#n es el número de caracteres que va a leer+

archivo = open("archivo.txt","r")

cadena = archivo.read(4)
print(cadena)

cadena2 = archivo.read()
print(cadena2)

#Leer líneas

#readline() -> lee un archivo línea a línea

while True:
	linea = archivo.readline()
	if not linea:
		break
	print(linea)
archivo.close()

# ReadLines -> lee todas las líneas y las regresa como una lista

archivo = open("archivo.txt","r")

lineas = archivo.readlines()
numLinea = 0
for var in lineas:
	numLinea += 1
	print(numLinea,var)

#### ESCRITURA DE ARCHIVOS
##  write()

archivo = open("archivo.txt","w")
archivo.write("Sobreescirbí el archivo\n")
archivo.write("Ya no hay algo antes que yo") ##BORRA EL CONTENIDO Y LO REESCRIBE

archivo.close()

# writelines() -> escribe un número de cadenas

lista = ["lunes","martes","miércoles","jueves","viernes","99"] #Solo acepta cadenas.
archivo = open("archivo.txt","w")

archivo.writelines(archivo)

archivo.close()

## FUNCIONES PARA HACER USO DEL APUNTADOR

# seek(numero) -> desplaza el puntero a una posición del archivo
archivo = open ("archivo.txt","r")

archivo.seek(5) #Mueve el puntero al quinto byte (quinto caracter)

cadena1 = archivo.read(5) #Lee los siguientes 5 caracteres

print (archivo.tell())
print(cadena1) 

archivo.close()



