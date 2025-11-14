class Cachorro:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade


    def latir(self):
            return "Latido"
        


cachorro = Cachorro("Doginho",35)

print(cachorro.latir())