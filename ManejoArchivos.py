#Abrir archivo
#open(ruta, modo de abirlo)

#Modos de apertura
#r->read, lectura, el archivo debe existir 

#w->write, escritura, si el archivo no existe lo crea, si existe lo sobreescribe

#a->append, añadir, agrega datos al final del archivo

# + -> r y w. 

#Abrir un archivo
#Por dafault en modo lectura

objeto = open("archivo.txt")
#Se abre el archivo en modo escritura

objeto = open("archivo.txt","w")

#Cerrar archivo

objeto.close()
objeto.close()

#Leer

#read-> lee todo el archivo
#n es el número de caracteres que va a leer+

archivo = open("archivo.txt","r")

cadena = archivo.read(4)
print(cadena)

cadena2 = archivo.read()
print(cadena2)

#Leer líneas

