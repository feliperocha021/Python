# A herança é um dos pilares da Programação Orientada a Objetos (POO). Ela permite que uma classe filha (subclasse) reutilize atributos e métodos de uma classe pai (superclasse).

# Tipos de herança em Python:
# Simples → uma classe herda de apenas uma superclasse.

# Múltipla → uma classe herda de várias superclasses.

# Multinível → uma classe herda de outra que também herdou de uma terceira.

# Hierárquica → várias subclasses herdam da mesma superclasse.

from animal import Dog, Cat, Mouse

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
cat.eat()
mouse.sleep()
dog.speak()
cat.speak()