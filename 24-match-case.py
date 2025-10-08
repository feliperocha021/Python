# Ele funciona de forma parecida com o switch-case de outras linguagens, mas é mais poderoso, permitindo verificar valores, tipos, padrões em listas, dicionários e até aplicar condições extras (guards).
# O _ funciona como um coringa (default), que casa com qualquer valor.

def check_number(x):
    match x:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's something else")

check_number(10)
check_number(30) 

def check_color(color):
    match color:
        case "red" | "blue" | "green":
            print("It's a primary color")
        case _:
            print("It's another color")

check_color("blue")
check_color("yellow")

def check_age(age):
    match age:
        case x if x < 18:
            print("Minor")
        case x if 18 <= x < 65:
            print("Adult")
        case _:
            print("Senior")

check_age(15)
check_age(30)
check_age(70)
