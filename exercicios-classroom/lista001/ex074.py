# 74.Verifique se uma string é um endereço de e-mail válido.

string = input("Digite uma string: ")

def validar_email(email):
    # se tem '@'
    if email.count('@') != 1:
        return False

    # separar usuário de domínio
    usuario, dominio = email.split('@')

    # ver se alguma parte está vazia
    if not usuario or not dominio:
        return False

    # ver se tem ponto no domínio
    if not '.' in dominio:
        return False

    # ver se o ponto não está no início ou no fim do domínio
    if dominio.startswith('.') or dominio.endswith('.'):
        return False

    # ver se o nome de usuário ou domínio tem espaços
    if ' ' in usuario or ' ' in dominio:
        return False

    return True

if validar_email(string):
    print("A string é um endereço de e-mail válido.")
else:
    print("A string não é um endereço de e-mail válido.")