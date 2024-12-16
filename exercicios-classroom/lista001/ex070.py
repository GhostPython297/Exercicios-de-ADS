# 70.Verifique se uma string contém apenas letras e números.

string = input("Digite uma string: ")

if string.isalnum():
    print("A string contém apenas letras e números.")
else:
    print("A string contém caracteres inválidos.")