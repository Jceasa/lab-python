# Mostre o erro comum: def func(lista=[]): ...

def func(item, lista=[]):
    lista.append(item)
    return lista

print(func(1))
print(func(2))
print(func(3))

# Nunca devemos usar listas, dicionários ou sets como valor padrão em funções, 
# porque eles são criados uma vez só, e não a cada chamada.