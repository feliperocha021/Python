# Um método estático é um método definido dentro de uma classe, mas que não recebe automaticamente a instância (self) nem a classe (cls) como primeiro argumento.

# Ele é criado com o decorador @staticmethod.

# Pode ser chamado tanto pela classe quanto por uma instância, mas não tem acesso direto a atributos da instância ou da classe.

# É útil quando você quer agrupar uma função relacionada logicamente à classe, mas que não depende de dados da instância ou da classe.

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):  # instance method
        print(f"{self.name} is barking!")

    @staticmethod
    def general_info():  # static method
        print("Dogs are loyal animals.")

dog = Dog("Buddy")
dog.bark()
dog.general_info()
Dog.general_info()
