import random

def gerar_numero_aleatorio():
    """
    Gera um número aleatório entre 1 e 100.

    Retorna:
        int: Um número inteiro aleatório entre 1 e 100.
    """
    return random.randint(1, 100)

# Exemplo de uso
numero_aleatorio = gerar_numero_aleatorio()
print(f"Número aleatório gerado: {numero_aleatorio}")
