import re

if re.match("hola","hola"):
	print("Hizo match1")

if re.match(".ola","hola"):
	print("Hizo match2")

if re.match("\.ola",".ola"):
	print("Hizo match3")
if re.match("python|jython|cython","cython"):
	print("Hizo match4")
if re.match("(p|j|c)ython","python"):
	print("Hizo match5")
if re.match("[hjw]ola","hola"):
	print("Hizo match6")

if re.match("cadena[0-9]","cadena8"): #Pudes tomar un núemro que sea implícito. Puede recibir el que esté dentro del rango
	print("Hizo match7")