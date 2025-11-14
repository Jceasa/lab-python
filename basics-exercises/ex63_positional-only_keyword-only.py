# Crie uma função com / e * para forçar tipos de passagem.

def dividir(a, b, /):
    return a / b

#print(dividir(10, 2))
#print(dividir(a=10, b=2))

def apresentar(nome, *, idade, cidade):
    print(f"{nome} tem {idade} anos e mora em {cidade}.")


print(apresentar("Júlio", idade=34, cidade="Trindade-GO"))

