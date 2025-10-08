# Exceções são erros que acontecem durante a execução do programa. Se não forem tratadas, o programa interrompe a execução e mostra uma mensagem de erro (traceback).

# O tratamento de exceções permite capturar esses erros e decidir o que fazer: mostrar uma mensagem amigável, tentar novamente, usar um valor padrão, etc.

# Estrutura principal:
# try → bloco onde você coloca o código que pode gerar erro.

# except → bloco que captura e trata o erro.

# else → executa se nenhuma exceção ocorrer.

# finally → executa sempre, independentemente de erro ou não (útil para liberar recursos, fechar arquivos, etc.).

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

try:
    value = int("abc")
except ValueError:
    print("Invalid conversion to integer")
except TypeError:
    print("Type error occurred")

try:
    num = int("42")
except ValueError:
    print("Conversion failed")
else:
    print(f"Conversion successful: {num}")

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print("File read successfully")
finally:
    print("Closing file (if it was opened)")
    try:
        file.close()
    except:
        pass

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    print(withdraw(100, 200))
except ValueError as e:
    print(f"Error: {e}")
