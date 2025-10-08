# Regra LEGB:

# A resolução de nomes segue a regra LEGB, na ordem:

# Local: nomes definidos dentro da função atual.

# Enclosing (envolvente): nomes em funções externas, quando há funções aninhadas.

# Global (módulo): nomes definidos no topo do arquivo (módulo) atual.

# Built-in: nomes da biblioteca interna do Python (por exemplo, len, print, range).

# Palavras-chave global e nonlocal:

# global: indica que você quer ler/escrever um nome no escopo global do módulo dentro de uma função. Sem isso, uma atribuição cria um nome local.

# nonlocal: permite acessar e modificar um nome no escopo envolvente (não global) em funções aninhadas. Útil para closures.

# Observações:

# Métodos e classes: o corpo da classe tem seu próprio namespace de atributos; dentro de métodos, nomes simples seguem LEGB (não buscam automaticamente atributos da classe sem self ou o nome da classe).

# Loops: for e while não criam um novo escopo; variáveis do loop permanecem acessíveis após o loop.

# Compreensões: em Python 3, compreensões de lista, dict e set têm escopo próprio; variáveis internas não “vazam” para fora.

pi = "global pi"

def outer():
    pi = "enclosing pi"
    def inner():
        pi = "local pi"
        print(pi)  # local
    inner()
    print(pi)      # enclosing

outer()
print(pi)          # global

counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)  # 2

def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = make_counter()
print(c())  # 1
print(c())  # 2
