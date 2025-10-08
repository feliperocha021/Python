# O @property é um decorador que transforma um método em um atributo de leitura.

# Isso permite que você acesse um método como se fosse um atributo, sem precisar usar parênteses.

# Ele é muito usado para encapsular atributos privados (normalmente com _nome) e fornecer uma interface mais limpa e controlada.

# Com ele, você pode:

# Criar getters (para ler valores).

# Criar setters (para validar ou modificar valores antes de atribuí-los).

# Criar deleters (para controlar a exclusão de atributos).

class Person:
    def __init__(self, name):
        self._name = name  # private attribute by convention

    @property
    def name(self):
        return self._name

p = Person("Alice")
print(p.name)  # Access like an attribute, but it's actually a method

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15°C is not possible")
        self._temperature = value

c = Celsius()
c.temperature = 25   # calls setter
print(c.temperature) # calls getter -> 25

# c.temperature = -300  # would raise ValueError

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

item = Product(100)
print(item.price)  # 100
item.price = 50    # setter
del item.price     # deleter
