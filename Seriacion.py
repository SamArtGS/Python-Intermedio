# SERIALIZACION - TRANSFORMAR UN OBJETO
#determinado en un exto en base a un lenguaje, para ser
#almacenado o bien transferido y por último, restablecido al objeto original

import pickle #Pasar nuestros datos a un archivo

# dump() - método se va a sealizar el contanido de un archivo

# load() - toma un objeto file, lee los datos sealizados, crea un nuevo objeto Python, recrea los datos serializados
# en el nuevo objeto y devuelve el objeto

dic ={"cadena":"ggg","tupla":(1,2,3),"lista":[4,5,6],"booleano":True} 

with open("datos.pickle","wb") as f:
	pickle.dump(dic,f) #Transformación a un código binario

with open("datos.pickle","rb") as f:
	datos = pickle.load(f)

print(datos)


## dumb(), loads()
## NO queremos que se guarde en los archivos, se guarde en la memoria

cadena = "Python AM"

b = pickle.dumps(cadena)
print(type(b))

cadena2 = pickle.loads(b)
print(cadena2)


