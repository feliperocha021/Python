# O super() é uma função usada em herança para chamar métodos da superclasse (classe pai) dentro de uma subclasse (classe filha).

# Ele é muito usado em construtores (__init__), mas pode ser aplicado em qualquer método herdado.

# A grande vantagem é que você não precisa escrever o nome da classe pai diretamente, o que torna o código mais flexível e compatível com herança múltipla.

# O Python usa a MRO (Method Resolution Order) para decidir qual classe pai será chamada quando usamos super().

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)
print(dog.breed)

class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    def greet(self):
        super().greet()
        print("I'm a student.")

s = Student()
s.greet()
