# 72.Verifique se uma string é uma palavra reservada em Python.

import keyword

string = input("Digite uma string: ")

if keyword.iskeyword(string):
    print("A string é uma palavra reservada em Python.")
else:
    print("A string não é uma palavra reservada em Python.")