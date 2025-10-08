# List comprehension é uma forma concisa e elegante de criar listas em Python a partir de um iterable (lista, tupla, string, range, etc.), aplicando transformações e até filtros em uma única linha.

# É como um atalho para loops for combinados com append.

# nova_lista = [expressão for item in iterável if condição]

# expressão → o que você quer colocar na nova lista.

# item → cada elemento do iterável.

# condição (opcional) → filtro para decidir se o item entra ou não.

squares = [x**2 for x in range(6)]
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

word = "python"
uppercase_letters = [letter.upper() for letter in word]
print(uppercase_letters)

result = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(result)

matrix = [[1, 2, 3], [4, 5, 6]]
flatten = [num for row in matrix for num in row]
print(flatten)
