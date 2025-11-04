# Escreva "Olá, mundo!" em um arquivo texto e depois leia e imprima.


with open("ola-mundo.txt" , 'w') as arquivo:
    arquivo.write("Olá, Mundo")

with open("ola-mundo.txt", 'r') as arquivo:
    arquivo = arquivo.read()
    print(arquivo)