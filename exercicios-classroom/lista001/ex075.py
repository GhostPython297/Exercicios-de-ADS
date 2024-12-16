# 75.Crie uma string e remova todos os sinais de pontuação.

string = input("Digite uma string: ")

string_sem_pontuacao = ""

for caractere in string:
    if caractere.isalnum() or caractere.isspace():
        string_sem_pontuacao += caractere

print(f'A string "{string}" sem pontuação é: {string_sem_pontuacao}')