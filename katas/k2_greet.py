# Crie uma função que forneça uma saudação personalizada. 
# Esta função recebe dois parâmetros: 'name' e 'owner'.
# Utilize condicionais para retornar a mensagem correta:
# caso:  nome é igual a proprietário , retornar: Olá, chefe'
# caso: de outra forma , retornar: "Olá, visitante"


def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'