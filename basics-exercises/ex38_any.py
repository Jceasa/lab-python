# Verifique se qualquer número em [0, 0, 5] é maior que 3.

lista = [0, 0, 5]

for number in lista:
    print(any(number > 3 for number in lista))