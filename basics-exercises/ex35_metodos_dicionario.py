# Imprima chaves, valores e itens de um dicionário.

dicionario = {
    "nome": "Josias",
    "idade": 28,
    "sexo": "Masculino"
}

for i in dicionario.keys():
    print(f"Chave: {i}")

for i in dicionario.values():
    print(f"Valor: {i}")

for i in dicionario.items():
    print(f"items(): {i}")