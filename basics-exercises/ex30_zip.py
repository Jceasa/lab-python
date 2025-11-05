# Combine duas listas: nomes = ["Ana", "Bia"] e idades = [20, 25] em tuplas.

nomes = ["Ana", "Bia"]
idades = [20, 25]

combine = zip(nomes, idades)


for i in combine:
    print(i)