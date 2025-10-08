# Os membership operators são usados para verificar se um valor está presente (ou não) dentro de uma sequência ou coleção (como list, tuple, set, dict, str). Eles retornam sempre um booleano (True ou False).

# Tipos de membership operators
# in → retorna True se o valor estiver presente.

# not in → retorna True se o valor não estiver presente.

fruits = ["apple", "banana", "grape"]

print("apple" in fruits)
print("orange" in fruits)
print("pear" not in fruits)


text = "Python is amazing"

print("Python" in text)
print("java" in text)
print("amazing" not in text)

vowels = {"a", "e", "i", "o", "u"}

print("a" in vowels)
print("y" not in vowels)

student = {"name": "Anna", "age": 20}

print("name" in student)       # True (key exists)
print("Anna" in student)       # False (value, not key)
print("age" not in student)    # False
print("Anna" in student.values())  # True
