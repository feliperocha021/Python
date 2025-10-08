"""
Multithreading significa rodar várias threads dentro de um mesmo processo, permitindo que tarefas sejam executadas de forma concorrente.

Em Python, usamos principalmente o módulo threading para criar e gerenciar threads.

É especialmente útil em tarefas I/O-bound (como leitura/escrita de arquivos, chamadas de rede, acesso a banco de dados), porque enquanto uma thread espera, outra pode continuar trabalhando.

Para tarefas CPU-bound (cálculos pesados), o multithreading em Python não traz grandes ganhos por causa do GIL (Global Interpreter Lock), que limita a execução de threads em paralelo. Nesse caso, o ideal é usar multiprocessing.
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in "ABCDE":
        print(f"Letter: {letter}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Done!")

def task(name):
    print(f"Task {name} starting")
    time.sleep(2)
    print(f"Task {name} finished")

# Create a pool with 2 worker threads
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(task, "A")
    executor.submit(task, "B")
    executor.submit(task, "C")

def square(num):
    print(f"Square of {num}: {num * num}")
    time.sleep(1)

def cube(num):
    print(f"Cube of {num}: {num * num * num}")
    time.sleep(1)

t1 = threading.Thread(target=square, args=(4,))
t2 = threading.Thread(target=cube, args=(4,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Finished calculations")