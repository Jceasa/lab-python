# Crie uma função que yield from uma lista.

frutas = ["Abacate","Pera","Cupuaçu","Morango"]

def generator_yeld_from(lista):
    yield from lista

gen = generator_yeld_from(frutas)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))