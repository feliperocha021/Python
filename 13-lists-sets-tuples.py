# List = [] ordenadas e mutáveis e aceita valores duplicados
# Set = {} desordenadas e imutáveis, mas pode adicionar e remover. Não aceita valores duplicados
# Tuple = () ordenada e imutáveis, aceita valores duplicados e é mais rápido

#LIST
print("=" * 50)
print("LIST")
print("=" * 50)

fruits = ["apple", "orange", "banana"]

print(fruits[::-1])
print(len(fruits))
fruits[0] = "pineapple"
fruits.append("apple")
fruits.remove("pineapple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
print("pineapple" in fruits)

for fruit in fruits:
  print(fruit, end=" ")

print(fruits.index("apple"))

# SET
print("=" * 50)
print("SET")
print("=" * 50)

fruits = {"apple", "orange", "banana"}

print(len(fruits))
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()

print(fruits)

# TUPLES
print("=" * 50)
print("TUPLES")
print("=" * 50)

fruits = ("apple", "orange", "banana")
print(len(fruits))
print("pineapple" in fruits)
print(fruits.index("apple"))
print(fruits.count("apple"))

for fruit in fruits:
  print(fruit, end=" ")