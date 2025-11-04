# Divida "maçã,banana,laranja" em lista e junte com " - ".

words = "maça,banana,laranja"

divide = words.split(',')

join = '-'.join(divide)

print(join)