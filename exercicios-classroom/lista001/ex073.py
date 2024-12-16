# 73.Crie uma string e substitua todas as letras minúsculas por maiúsculas e vice-versa.

string = input("Digite uma string: ")

string_alterada = ""

for caractere in string:
    if caractere.isupper():
        caractere_alterado = caractere.lower()
    else:
        caractere_alterado = caractere.upper()
    string_alterada += caractere_alterado

print(f'A string "{string}" alterada é: {string_alterada}')