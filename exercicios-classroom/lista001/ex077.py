# 77.Crie uma string e converta todos os caracteres para hexadecimal.

string = input("Digite uma string: ")

string_hexadecimal = ""

# se o usuário digitar "AB", o código executará as seguintes etapas:
# ord('A') retorna 65, e hex(65) retorna '0x41', portanto hex(65)[2:] retorna '41'.
# ord('B') retorna 66, e hex(66) retorna '0x42', portanto hex(66)[2:] retorna '42'.
# string_hexadecimal resultará em '4142'.
for caractere in string:
    caractere_hexadecimal = hex(ord(caractere))[2:]
    string_hexadecimal += caractere_hexadecimal

print(f'A string "{string}" em hexadecimal é: {string_hexadecimal}')