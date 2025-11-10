# Crie uma função que aceita **kwargs e imprime nome e idade.

def saudacao(**kwargs):
    info = {}
    for chave , valor in kwargs.items():
        info[chave] = valor
    return info 


print(saudacao(nome="Júlio" , idade=25))

