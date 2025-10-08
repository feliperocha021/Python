# não precisamos verificar explicitamente se um objeto é de uma classe específica — basta que ele implemente os métodos/atributos esperados.

# Características:
# Foco no comportamento (métodos/atributos), não na herança ou tipo exato.

# Torna o código mais flexível e desacoplado.

# Muito usado em polimorfismo e interfaces implícitas.

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(obj):
    # No type check, just call the method
    obj.quack()

duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)
