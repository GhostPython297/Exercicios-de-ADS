import time

def funcao_exemplo():
    soma = 0
    for i in range(1000000):
        soma += i
    return soma

def medir_tempo_execucao():
    inicio = time.time()  # Tempo inicial
    funcao_exemplo()
    fim = time.time()  # Tempo final
    print(f"Tempo de execução: {fim - inicio} segundos")

# Chamar a função
medir_tempo_execucao()
