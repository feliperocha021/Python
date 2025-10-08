name = input("Enter your full name: ")
print(len(name))

# Retorna o índice da primeira ocorrência, caso não encontre retorna -1
print(name.find("a"))

# Retorna o índice da última ocorrência, caso não encontre retorna -1
print(name.rfind("a"))

# O primeiro caratere é transformada em maiúscula
print(name.capitalize())

# Todos os caracteres são transformadas em maiúsculas
print(name.upper())

# Todos os caracteres são transformadas em minúsculas
print(name.lower())

# Retorna true se todos os carcteres forem números
print(name.isdigit())

# Retorna true se todos os carcteres forem letras do alfabeto
print(name.isalpha())

# Retorna a contagem de uma substring em uma string
print(name.count("a"))

# Trocar o valor de uma substring em uma string
print(name.replace("a", "e"))

# Remove espaços em branco no inicio e final
print(name.strip())

# Exibe todas as funções de string
print(help(str))
