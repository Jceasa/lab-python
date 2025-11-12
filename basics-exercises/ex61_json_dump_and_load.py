# Salve um dicionário em JSON e carregue de volta.

import json


alunos = {
    "Aluno": "Julio",
    "Idade": 23,
    "Local": "Grécia",
}

with open('dados.json', 'w', encoding="utf-8") as arquivo:
    json.dump(alunos,arquivo, indent=4, ensure_ascii=False)

print("Arquivo salvo com sucesso!")

with open("dados.json", 'r' , encoding='utf-8') as arquivo:
    dados_lido = json.load(arquivo)

print(dados_lido)
