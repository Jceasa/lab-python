set1 = {23 , 1, 2000, 50}
set2 = {10 , 10, 2010, 50}

uniao = set.union(set1,set2) ## Método set.union
intersecao = set1 & set2 ## Método com o operador de interseção ou podemos usar intersection(set1,set2)
diferenca = set1 - set2 ## Elementos em set1 que não estã no set2
use_clear = uniao.clear()

#print(f"Union: {uniao}")
#print(intersecao)
#print(diferenca)
#print(use_clear)