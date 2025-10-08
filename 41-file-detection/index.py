# Verificar se um arquivo ou diretório existe, identificar seu tipo (arquivo ou pasta), ou até mesmo procurar arquivos em um diretório. Isso é muito útil em situações como:

# Conferir se um arquivo existe antes de abri-lo.

# Diferenciar entre arquivo e diretório.

# Procurar arquivos por nome ou padrão em uma pasta.

# As bibliotecas mais usadas para isso são:

# os → funções básicas de manipulação de arquivos e diretórios.

# os.path → checagem de existência, tipo de caminho.

# pathlib → interface orientada a objetos para lidar com caminhos.

# glob → busca de arquivos por padrões (ex.: *.txt).

import os
from pathlib import Path
import glob

file_path = "41-file-detection/example.txt"

if os.path.exists(file_path):
    print(f"'{file_path}' exists")
    if os.path.isfile(file_path):
        print("It is a file")
    elif os.path.isdir(file_path):
        print("It is a directory")
else:
    print("Path does not exist")

path = Path("41-file-detection/example.txt")

if path.exists():
    print(f"{path} exists")
    if path.is_file():
        print("It is a file")
    elif path.is_dir():
        print("It is a directory")
else:
    print("Path does not exist")

def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None

result = find_file("example.txt", ".")
print(result if result else "File not found")

# Find all .txt files in current directory and subdirectories
files = glob.glob("**/*.txt", recursive=True)
print(files)
