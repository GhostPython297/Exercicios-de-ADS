def remover_duplicatas():
    numeros = list(map(int, input("Digite os números separados por espaço: ").split()))
    lista_sem_duplicatas = list(set(numeros))
    return lista_sem_duplicatas

# Chamar a função
print(remover_duplicatas())
