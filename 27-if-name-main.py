# Todo arquivo Python é considerado um módulo.

# Quando você executa um arquivo diretamente, o Python cria uma variável especial chamada __name__ e atribui a ela o valor "__main__".

# Se o arquivo for importado como módulo em outro arquivo, o __name__ recebe o nome do módulo (geralmente o nome do arquivo sem .py).

# O if __name__ == "__main__": serve para controlar o ponto de entrada do programa.

# O código dentro desse bloco só será executado quando o arquivo for rodado diretamente.

# Se o arquivo for importado, esse bloco não será executado.

# Isso é muito útil para:

# Criar scripts reutilizáveis (podem ser executados ou importados).

# Separar a lógica principal do código de funções e classes auxiliares.

# Evitar que código de teste rode quando o módulo for importado.


# file_one.py

""" def greet():
    print("Hello from file_one!")

if __name__ == "__main__":
    print("Running file_one directly")
    greet()

python file_one.py
>> Running file_one directly
>> Hello from file_one!

# file_two.py

import file_one

print("Now inside file_two")

python file_two.py
>> Hello from file_one!   # (executado ao importar, se não estivesse protegido pelo if)
>> Now inside file_two

Mas como usamos o if __name__ == "__main__": em file_one.py, a linha "Running file_one directly" não aparece quando importamos. """