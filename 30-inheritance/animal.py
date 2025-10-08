class Animal:
  def __init__(self, name):
    self.name = name
    self.is_alive = True

  def eat(self):
    print(f"{self.name} is eating")

  def sleep(self):
    print(f"{self.name} is sleeping")

class Dog(Animal):
  def speak(self):
    print("Wooof!")

class Cat(Animal):
  def speak(self):
    print("Meown!")

class Mouse(Animal):
  def speak(self):
    print("SQUEEK!")
