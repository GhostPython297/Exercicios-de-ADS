import time

# Função de exemplo
# Essa função soma os números de 0 a 999.999
# Ela é usada para medir o tempo de execução
# da função
def funcao_exemplo():
    soma = 0
    for i in range(1000000):
        soma += i
    return soma

# Função para medir o tempo de execução
# da função de exemplo
# Ela imprime o tempo de execução em segundos
# da função de exemplo
# Ela é usada para medir o tempo de execução
# da função
def medir_tempo_execucao():
    inicio = time.time()  # Tempo inicial
    funcao_exemplo()
    fim = time.time()  # Tempo final
    print(f"Tempo de execução: {fim - inicio} segundos")

# Chamar a função
medir_tempo_execucao()
