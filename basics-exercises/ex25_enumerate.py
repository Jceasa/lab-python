# Use enumerate para imprimir índice e valor de uma lista.

lista = ['javascript','golang','c#','c++']

for i , valor in enumerate(lista):
    print(f"{i + 1} - {valor}")