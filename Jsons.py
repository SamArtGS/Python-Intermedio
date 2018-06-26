import json

archivo_json = open("discos.json","r")
print(type(archivo_json))

informacion_discos = json.load(archivo_json)

print(type(informacion_discos))

for elemento in informacion_discos:
	print(elemento)
	print(type(elemento))

for elemento in informacion_discos:
	print(elemento["Nombre"])
	#print(type(elemento))

for elemento in informacion_discos:
	print(elemento["Singles"])

nuevo_disco = {
	"Artista": "Coldplay",
	"Canciones": 5,
	"Nombre": "A Rush Blood to the Head",
	"Singles": ["Clocks","The Scientist","Green Eyes","Warning Sing","In My Place"]
}


archivo_json = open("discos.json","w")
informacion_discos.append(nuevo_disco)
json.dump(informacion_discos,archivo_json)
