# Também podemos usar tuplas e sets

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

fruits[0] = "pineapple"

for collection in groceries:
  for food in collection:
    print(food, end=" ")
  print()
