# Herança múltipla acontece quando uma classe herda de duas ou mais superclasses ao mesmo tempo.

# Isso permite que a subclasse combine comportamentos e atributos de várias classes.

# É um recurso poderoso, mas precisa ser usado com cuidado para evitar ambiguidades.

# O problema clássico: Diamond Problem
# Imagine uma hierarquia em forma de diamante: uma classe A é herdada por B e C, e depois D herda de B e C.

# Se D chamar um método que existe em A, qual versão deve ser usada?

# O Python resolve isso com a MRO (Method Resolution Order), que define a ordem de busca de métodos e atributos.

# Você pode ver a MRO de uma classe com ClassName.__mro__ ou ClassName.mro().

""" 
class A:
    def action(self):
        print("Action from A")

class B(A):
    def action(self):
        print("Action from B")

class C(A):
    def action(self):
        print("Action from C")

class D(B, C):
    pass

d = D()
d.action()  # Action from B (because of MRO)

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
"""

class A:
    def action(self):
        print("A action")

class B(A):
    def action(self):
        print("B action")
        super().action()

class C(A):
    def action(self):
        print("C action")
        super().action()

class D(B, C):
    def action(self):
        print("D action")
        super().action()

d = D()
d.action()
