def remover_duplicatas():
    # map serve para transformar os elementos de uma lista em outro tipo
    # nesse caso, transformamos os elementos em int
    # split() separa os elementos da lista por espaço
    # set() remove as duplicatas
    # list() transforma o set em lista novamente
    numeros = list(map(int, input("Digite os números separados por espaço: ").split()))
    lista_sem_duplicatas = list(set(numeros))
    return lista_sem_duplicatas

# Chamar a função
print(remover_duplicatas())
