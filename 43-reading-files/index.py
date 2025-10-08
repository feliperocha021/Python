"""
Em Python, a leitura de arquivos é feita com a função open(), que retorna um objeto de arquivo. Você pode abrir o arquivo em diferentes modos:

'r' → leitura (padrão).

'rb' → leitura em modo binário (imagens, áudio, etc.).

Depois de abrir, você pode usar métodos como:

read() → lê todo o conteúdo de uma vez.

readline() → lê uma linha por vez.

readlines() → lê todas as linhas e retorna uma lista.

Iterar diretamente sobre o arquivo (for line in file).

É boa prática usar with open(...) porque ele fecha o arquivo automaticamente, mesmo em caso de erro.
"""

file_path = "43-reading-files/example.txt"
image_path = "43-reading-files/python-logo.png"

with open(file_path, "r") as f:
    content = f.read()
    print(content)

with open(file_path, "r") as f:
    for line in f:
        print(line.strip())  # strip() removes newline characters

with open(file_path, "r") as f:
    lines = f.readlines()
    print(lines)  # ['First line\n', 'Second line\n', 'Third line\n']

with open(file_path, "r") as f:
    first_five = f.read(5)  # reads first 5 characters
    print(first_five)

with open(image_path, "rb") as f:
    data = f.read()
    # print(data)
    print(len(data), "bytes read")
