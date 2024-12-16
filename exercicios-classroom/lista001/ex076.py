# 76.Verifique se uma string é uma data válida no formato DD/MM/AAAA.

data = input("Digite uma data (dd/mm/aaaa): ")

def validar_data(data):
    # se tem '/'
    if data.count('/') != 2:
        return False

    # separar dia, mês e ano
    dia, mes, ano = data.split('/')

    # ver se alguma parte está vazia
    if not dia or not mes or not ano:
        return False
    
    # ver se dia, mês e ano são números
    if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
        return False

    # ver se dia está entre 1 e 31
    if int(dia) < 1 or int(dia) > 31:
        return False

    # ver se mês está entre 1 e 12
    if int(mes) < 1 or int(mes) > 12:
        return False

    # ver se ano tem 4 dígitos
    if len(ano) != 4:
        return False

    return True

if validar_data(data):
    print("A string é uma data válida no formato DD/MM/AAAA.")
else:
    print("A string não é uma data válida no formato DD/MM/AAAA.")