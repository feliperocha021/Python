# O uso do keyword permite passar um parametro em qualquer posição, além de melhorar a legibilidade

def hello(greeting, title, first, last):
  print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr.", last="Squarepants", first="Spongebob",)

print("1", "2", "3", "4", "5", sep="-")