# Existem 4 tipos diferentes int, float, str, bool

first_name = ""
age = 25
height = 1.80
is_student = True

print(f"My name is {first_name}, I am {age} years olds and {height} meters tall")

# Typecasting
age = str(age)
age += "1"
print(age)

first_name = bool(first_name)
print(first_name)

print(type(age))
