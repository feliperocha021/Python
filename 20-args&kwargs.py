# O *args permite que você passe um número variável de argumentos posicionais para uma função.
# Dentro da função, esses argumentos são recebidos como uma tupla.

def soma(*args):
    return sum(args)

print(soma(1, 2))
print(soma(1, 2, 3, 4, 5))

# O **kwargs permite que você passe um número variável de argumentos nomeados (no formato chave=valor).
# Dentro da função, esses argumentos são recebidos como um dicionário.

def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} = {valor}")

mostrar_info(nome="Ana", idade=25, curso="Python")

# Podemos combinar parâmetros normais, *args e **kwargs na mesma função.
# A ordem sempre é: **parâmetros normais → *args → parâmetros nomeados → kwargs.

def exemplo(x, *args, y=0, **kwargs):
    print("x:", x)
    print("args:", args)
    print("y:", y)
    print("kwargs:", kwargs)

exemplo(10, 20, 30, 40, y=50, nome="John", ativo=True)
