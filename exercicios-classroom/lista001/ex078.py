# 78.Verifique se uma string é um endereço IP válido.

import ipaddress

def validar_ip(endereco_de_ip):
    # tenta converter o endereço de IP para um objeto ipaddress
    # se der erro, é porque o endereço de IP é inválido
    # se não der erro, é porque o endereço de IP é válido
    # e retorna True
    try:
        ip = ipaddress.ip_address(endereco_de_ip)
        return True
    except ValueError:
        return False

# pede para o usuário digitar um endereço de IP
endereco_ip = input("Digite um endereço de IP: ")

# verifica se o endereço de IP é válido
if validar_ip(endereco_ip):
    print("O endereço de IP é válido.")
else:
    print("O endereço de IP é inválido.")