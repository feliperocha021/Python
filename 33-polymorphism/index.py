# Tipos de polimorfismo em Python:
# Polimorfismo de operadores → o mesmo operador funciona de formas diferentes dependendo do tipo.

# Exemplo: + soma números, mas também concatena strings.

# Polimorfismo de funções embutidas → funções como len() funcionam com listas, strings, dicionários etc.

# Polimorfismo em classes (sobrescrita de métodos) → subclasses podem redefinir métodos da superclasse, e objetos diferentes respondem de forma distinta ao mesmo método.

class Bird:
    def info(self):
        print("I am a bird")

class Sparrow(Bird):
    def info(self):
        print("I am a sparrow")

class Penguin(Bird):
    def info(self):
        print("I am a penguin")

def describe(bird: Bird):
    bird.info()

describe(Sparrow())  # I am a sparrow
describe(Penguin())  # I am a penguin
