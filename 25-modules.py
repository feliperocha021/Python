# Um módulo em Python é simplesmente um arquivo .py que contém funções, classes e variáveis que podem ser reutilizadas em outros programas.

# Eles ajudam a organizar o código em partes menores e mais fáceis de manter.

# Existem quatro tipos principais:

# Módulos embutidos (já vêm com o Python, ex.: math, os, sys).

# Módulos da biblioteca padrão (parte do Python, mas precisam ser importados, ex.: json, re, csv).

# Módulos de terceiros (instalados via pip, ex.: requests, numpy, pandas).

# Módulos locais (arquivos .py que você mesmo cria).

import math as m

print(m.factorial(5))

from math import sqrt, pi

print(sqrt(25))
print(pi)

"""
Suponha que você crie um arquivo chamado mymodule.py:

# mymodule.py
def greet(name):
    return f"Hello, {name}!"
Agora, em outro arquivo Python:

# main.py
import mymodule

print(mymodule.greet("Jhon"))  # Hello, Jhon! 
"""