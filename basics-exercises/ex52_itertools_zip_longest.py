# Use zip_longest para combinar listas de tamanhos diferentes.

from itertools import zip_longest

nomes = ["Maria","Katia","Luana","Lorraine"]
frutas = ["abacaxi","maça","morango"]

print(*zip_longest(nomes,frutas))