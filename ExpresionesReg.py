import re

texto = "En esta cadena existe una palabra magica"

# RE --> Regular Expresions

print(re.search("magica",texto))

print(re.search("hola",texto))


palabra = "asistentes hola asistentes"

#Match devuelve un objeto match solamente si la coincidencia se encuenta al inicio

print(re.match("hola",palabra))

encontrado = re.search("hola",palabra)
encontrado.start()

print(encontrado.start())#Imprime la posición de inicio de la coincidencia
print(encontrado.end())#Imprime la posición del fin de la coincidencia


texto = "Hola amigo"
print(texto)
print(re.sub("amigo","amiga",texto))

texts = "Hola adios hola hola hola hola"

print(re.findall("hola",texts))









