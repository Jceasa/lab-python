# Use cada um desses métodos em um dicionário e mostre o resultado.

dicionario = {
    "Nome": "Abacaxi",
    "Preço": f"R$200",
    "Unidade": 200,
}

#value1 = dicionario.setdefault("Nome","Laranja")

##-----------------------------------------------

original_list = ["Golang","JavaScript","Python"]

copy_list = original_list.copy()

#print(copy_list)

##-----------------------------------------------

fruits_list = ["Abacaxi","Morango","Laranja"]

use_pop = fruits_list.pop()

#print(fruits_list)

##-----------------------------------------------

my_dict = {"name": "Alice", "age": 30, "city": "New York"}


use_popitem = my_dict.popitem()

#print(my_dict)

##-----------------------------------------------

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}

car.update({"color": "White"})

#print(car)