# Em Python, class variables (ou variáveis de classe) são atributos que pertencem à classe em si, e não a instâncias específicas.

# Isso significa que todas as instâncias compartilham o mesmo valor dessa variável, a menos que ela seja sobrescrita em uma instância.

# Diferem das instance variables (variáveis de instância), que são definidas dentro do __init__ e são únicas para cada objeto.

from student import Student

studnet1 = Student("Spongebob", 30)
studnet2 = Student("Patrick", 30)

print(studnet1.class_year)
print(studnet2.class_year)
print(Student.class_year)
print(Student.num_students)
