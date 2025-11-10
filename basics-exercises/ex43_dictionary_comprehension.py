# Crie {1:1, 2:4, 3:9} usando dict comprehension.

numbers = {x: x**2 for x in range(1,4)}

for chave, valor in numbers.items():
    print(f"{chave}: {valor}")

