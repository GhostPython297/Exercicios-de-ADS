# 79.Crie uma string e insira um caractere específico em intervalos regulares.

string = input("Digite uma string: ") # valor digitado pelo usuário
caractere = input("Digite um caractere: ") # caractere para inserção
intervalo = int(input("Digite um intervalo: ")) # intervalo para inserção

string_alterada = ""

for i in range(len(string)):
    # se o índice for um múltiplo do intervalo, insere o caractere
    # se não for, insere o caractere original
    # isso é feito para inserir o caractere em intervalos regulares
    # por exemplo, se o intervalo for 2, o caractere será inserido a cada 2 caracteres
    # se o intervalo for 3, o caractere será inserido a cada 3 caracteres e assim por diante
    if i % intervalo == 0:
        string_alterada += caractere
    else:
        string_alterada += string[i]

print(f'O resultado da string alterada é: {string_alterada}')