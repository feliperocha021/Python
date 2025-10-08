import random

number = random.randint(1, 7)
print(number, end=" ")
while not number == 7:
  number = random.randint(1, 7)
  print(number, end=" ")

print()

options = ("rock", "paper", "scissors")
print(random.choice(options))

numbers = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(numbers)
print(numbers)
