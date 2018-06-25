"""
Modulo que define la clase de Animal y dos clases que heredan de ellas (Gato,Perro)
para poder explicar el funcionamiento del polimorfismo
"""

class Animal:
  """
  Clase que abstrae a un animal
  """
  def saludar(self):
    """
    Metodo que permite a un animal saludar
    """
    print("Soy un animal")

  def comer(self):
    """
    Metodo que permite a un animal comer
    """
    print("Como algo")

class Perro(Animal):
  """
  Clase que abstrae el concepto de un perro
  Hereda de la clase animal
  """
  def comer(self):
    """
    Metodo que permite a un animal comer
    """
    print("Como DogChow")

class Gato(Animal):
  """
  Clase que abstrae el concepto de un gato
  """
  def comer(self):
    """
    Metodo que permite comer a un gato
    """
    print("Como Whiskas")


