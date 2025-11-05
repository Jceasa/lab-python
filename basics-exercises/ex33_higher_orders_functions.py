# Use map para dobrar todos os números de uma lista.

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

double = list(map(lambda n: n*2,numbers))

print(*double)
