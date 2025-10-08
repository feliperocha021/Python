"""
Em Python, escrever em arquivos é feito com a função open(), que retorna um objeto de arquivo. Você precisa passar dois argumentos principais:

Nome do arquivo (ou caminho).

Modo de abertura:

'w' → escrita (cria o arquivo ou sobrescreve se já existir).

'a' → append (acrescenta conteúdo ao final do arquivo).

'x' → cria um novo arquivo, mas gera erro se já existir.

'b' → modo binário (ex.: imagens, áudio).

't' → modo texto (padrão).

É boa prática usar o gerenciador de contexto with, porque ele fecha o arquivo automaticamente, mesmo em caso de erro.
"""

file_path = "42-writing-files/example.txt"

with open(file_path, "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a new line.\n")

lines = ["First line\n", "Second line\n", "Third line\n"]

with open(file_path, "w") as f:
    f.writelines(lines)

with open(file_path, "a") as f:
    f.write("Adding another line at the end.\n")