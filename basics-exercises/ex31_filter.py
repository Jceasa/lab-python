# Filtre números pares de uma lista usando filter e lambda.

numbers = [1,2,3,4,5,6,7,8,9,10]

pair_numbers = filter(lambda x: x % 2 == 0, numbers)

print(pair_numbers)

for i in pair_numbers:
    print(i)