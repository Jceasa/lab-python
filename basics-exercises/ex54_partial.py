# Crie uma função soma_10 que soma 10 a qualquer número usando partial.

from functools import partial

def soma_10(a ,ten):
    return a + ten


soma10 = partial(soma_10, ten=10)

print(soma10(15))