# Crie uma variável global e tente alterá-la dentro de uma função sem global.

variavel_global = 8


def soma(n1,n2):
    variavel_global = 10
    print(variavel_global)
    return int(n1 + n2)


print(soma(2,2))