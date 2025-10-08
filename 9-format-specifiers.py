price1 = 3.14159
price2 = -9870.655
price3 = 12.34

# Precisão de 2 casas decimais
print(f"Price 1 is ${price1:.2f}")

# Adicona 10 espaços a esquerda e caso sejam em branco substitua por 0
print(f"Price 2 is ${price2:010}")

# Adicione 10 espaços a direita
print(f"Price 3 is ${price3:<10}<-")

# Adicione 10 espaços a esquerda e caso sejam em branco substitua por 0
print(f"Price 3 is ${price3:>010}")

# Alinhamento central de 10 espaços
print(f"Price 3 is ${price3:^10}")

# Adicionando sinal
print(f"Price 2 is ${price2:+}")

# Espaços de 2 pontos
print(f"Price 2 is ${price2:,.2f}")