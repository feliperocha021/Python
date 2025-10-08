# são funções internas do Python que começam e terminam com __.

# Eles permitem personalizar o comportamento de objetos em situações comuns, como:

# Criação e inicialização de objetos (__new__, __init__)

# Representação em string (__str__, __repr__)

# Operadores aritméticos (__add__, __sub__, __mul__, etc.)

# Comparações (__eq__, __lt__, __gt__, etc.)

# Iteração (__iter__, __next__)

# Contexto (__enter__, __exit__)

class Person:
    def __init__(self, name, age):   # called when creating an object
        self.name = name
        self.age = age

    def __str__(self):               # called by print() or str()
        return f"{self.name} is {self.age} years old"

    def __repr__(self):              # called by repr() or in the REPL
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(p)
print(repr(p))

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):   # + operator
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # - operator
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)

print(v1 + v2)
print(v2 - v1)
