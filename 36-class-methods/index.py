# Um class method é um método que está vinculado à classe e não a uma instância específica.

# Ele é definido com o decorador @classmethod.

# Diferente dos métodos de instância (que recebem self), os métodos de classe recebem automaticamente a classe como primeiro argumento, chamado por convenção de cls.

# Isso significa que eles podem acessar e modificar variáveis de classe, mas não variáveis de instância.

# Quando usar:
# Quando você precisa de um método que afete a classe inteira, e não apenas um objeto.

# Para criar métodos de fábrica (factory methods), que retornam novas instâncias da classe de formas alternativas.

# Para trabalhar com herança, já que cls garante que o método funcione corretamente em subclasses.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        from datetime import date
        age = date.today().year - birth_year
        return cls(name, age)  # creates a new instance

p1 = Person("Alice", 30)
p2 = Person.from_birth_year("Bob", 1995)

print(p1.name, p1.age)
print(p2.name, p2.age)

class Animal:
    species = "Generic Animal"

    @classmethod
    def describe(cls):
        print(f"This is a {cls.species}")

class Dog(Animal):
    species = "Dog"

class Cat(Animal):
    species = "Cat"

Dog.describe()
Cat.describe()
