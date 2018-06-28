import sqlite3

conexion = sqlite3.connect("Jarocho.db")
cursor = conexion.cursor()

def insertar_en_tabla():
	nombre = input("Nombre del empleado: ")
	apellido = input("apellido: ")
	descripcion = input("descripcion: ")
	query = """INSERT INTO empleados VALUES ("{0}","{1}","{2}")""".format(nombre,apellido,descripcion)
	cursor.execute(query)

def crear_tabla():
	cursor.execute("""CREATE TABLE empleados (nombre TEXT,apellido TEXT,descripcion TEXT)""")

crear_tabla()
insertar_en_tabla()