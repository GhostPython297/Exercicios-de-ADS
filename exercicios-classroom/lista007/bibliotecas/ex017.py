# e) Use a biblioteca statistics para calcular a média, mediana e moda de uma lista de
# números.

import statistics

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

media = statistics.mean(lista)
mediana = statistics.median(lista)
moda = statistics.mode(lista)

print(f'A média da lista é: {media}')
print(f'A mediana da lista é: {mediana}')
print(f'A moda da lista é: {moda}')