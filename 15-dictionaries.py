# Um dicionário consiste em pares de valores-chave.
# Eles são ordenadose mutáveis e não permite duplicatas

capitals = {"USA": "Washington D.C",
             "India": "New Delhi",
             "China": "Beijing",
             "Russia": "Moscow"}

# Acessar
print(capitals.get("USA"))

# Atualizar e/ou criar
capitals.update({"German": "Berlin"})
capitals["German"] = "Berlin"

# Remover
capitals.pop("China")

# Remover último
capitals.popitem()

# Remover tudo
# capitals.clear()


for key in capitals.keys():
  print(capitals[key],  end=" ")

for key, value in capitals.items():
  print()