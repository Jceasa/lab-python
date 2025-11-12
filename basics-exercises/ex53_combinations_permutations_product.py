# Gere todas as combinações de 2 letras de "ABC".

from itertools import combinations

frutas = ["Abacate","Caju","Caja-manga","Cupuaçu"]

for combinationWord in combinations(frutas,2):
    print(combinationWord)

