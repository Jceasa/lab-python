# Use dir() em uma string. Use hasattr e getattr em um objeto.

name = "Kol"

#print(dir(name))

class Alunos:
    def __init__(self,nome):
        self.nome = nome

p = Alunos("Júlio")

#print(hasattr(p, "nome")) #Has atribute = True
#print(hasattr(p, "idade")) #Has atribute = False

print(getattr(p, "nome"))
print(getattr(p, "idade", "Idade não informada!"))