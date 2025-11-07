#Você consegue encontrar a agulha no palheiro?
#Escreva uma função findNeedle()que receba uma lista de array cheia de lixo, mas que contenha um único elemento."needle"
#Após a sua função encontrar a agulha, ela deverá retornar uma mensagem (em formato de texto) que diga:
# f"found the needle at position: {needle}"

def find_needle(haystack):
    for indice, word in enumerate(haystack):
        if word == 'needle':
            return f"found the needle at position: {indice}"
        

print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))