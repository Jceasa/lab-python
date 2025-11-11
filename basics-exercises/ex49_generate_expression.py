# Crie um generator que gera quadrados de 1 a 5.

quadrados_gen = (x**2 for x in range(1,5))

print(next(quadrados_gen))
print(next(quadrados_gen))
print(next(quadrados_gen))
print(next(quadrados_gen))