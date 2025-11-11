# Crie uma função geradora que yield números de 0 a n.

def numbers_generator(n):
    print("Começando...")
    for i in range(0,n):
        yield i 
    print("Fim..")


gen = numbers_generator(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))