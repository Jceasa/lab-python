# Crie uma classe Pessoa com nome e idade. Use __init__.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá meu nome é {self.nome}, é tenho {self.idade} anos!"
    


if __name__ == "__main__":
    pessoa1 = Pessoa("Júlio César", 25)
    print(pessoa1.saudacao())
