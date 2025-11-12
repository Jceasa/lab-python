# Use reduce para somar todos os números de uma lista.   

from functools import reduce

number = [12,34,59,100,9,44]
soma = reduce(lambda x,y: x + y, number)

print(soma)