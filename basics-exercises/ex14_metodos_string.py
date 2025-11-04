input_user = input("Digite algo: ")

if input_user.isnumeric():
    print("Sim, é númerico")
elif input_user.isupper():
    print("A frase e composta de letras maiúsculas")
elif input_user.isalpha():
    print("Contém apenas letras")
    