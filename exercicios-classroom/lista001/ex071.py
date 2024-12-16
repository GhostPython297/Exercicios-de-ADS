# 71.Crie uma string e converta todos os caracteres para binário.

string = input("Digite uma string: ")

string_binaria = ""

# se o usuário digitar "AB", o código executará as seguintes etapas:
# 1. ord('A') retorna 65, e bin(65) retorna '0b1000001',
# portanto bin(65)[2:] retorna '1000001'.
# 2. ord('B') retorna 66, e bin(66) retorna '0b1000010',
# portanto bin(66)[2:] retorna '1000010'.
# 3. string_binaria resultará em '10000011000010'.
for caractere in string:
    caractere_binario = bin(ord(caractere))[2:]
    string_binaria += caractere_binario

print(f'A string "{string}" em binário é: {string_binaria}')
