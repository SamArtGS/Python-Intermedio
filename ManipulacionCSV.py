#Trabajo con archivos en CSV
import csv
import random
archivos_csv = open("values.csv","w")
escritor = csv.writer(archivos_csv)

escritor.writerow(("Valor","25%","50%","75%")) ## Método que escribe un renglón

for i in range(1000):
	valor = random.randint(0,127)
	cuarto = valor * 0.25
	medio = valor * 0.5
	trescuartos = valor * .75
	row = [valor, cuarto, medio, trescuartos]
	escritor.writerow(row)

lista = open("lista.csv","w")
campos = ["id","nombre","promedio"]

escritor = csv.DictWriter(lista,fieldnames=campos)
escritor.writeheader()
escritor.writerow({"id":1,"nombre":"Aldo","promedio":8})
lista.close()


lista = open("lista.csv","r")
lector = csv.DictReader(lista)

for elemento in lector:
	print(elemento["nombre"])


