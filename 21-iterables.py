# Um iterable é qualquer objeto em Python que pode ser percorrido item por item em um loop (for, while com iter(), etc.).

# Em termos técnicos: é um objeto que implementa o método especial __iter__() ou __getitem__().

# Exemplos clássicos: list, tuple, str, dict, set, arquivos abertos, e até objetos que você mesmo cria.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
  print(number, end=" ")
