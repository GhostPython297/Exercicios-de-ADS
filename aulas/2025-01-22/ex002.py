## cédulas

## Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

## Entrada
## O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

## Saída
## Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

valor = int(input())
valor_inicial = valor

notas_de_100 = 0
notas_de_50 = 0
notas_de_20 = 0
notas_de_10 = 0
notas_de_5 = 0
notas_de_2 = 0
notas_de_1 = 0

# conta notas de 100
while valor >= 100:
    notas_de_100 += 1
    valor = valor - 100

# conta notas de 50
while valor >= 50:
    notas_de_50 += 1
    valor = valor - 50

# conta notas de 20
while valor >= 20:
    notas_de_20 += 1
    valor = valor - 20

# conta notas de 10
while valor >= 10:
    notas_de_10 += 1
    valor = valor - 10

# conta notas de 5
while valor >= 5:
    notas_de_5 += 1
    valor = valor - 5

# conta notas de 2
while valor >= 2:
    notas_de_2 += 1
    valor = valor - 2

# conta notas de 1
while valor >= 1:
    notas_de_1 += 1
    valor = valor - 1


print(valor_inicial)
print(f"{notas_de_100} nota(s) de R$ 100,00")
print(f"{notas_de_50} nota(s) de R$ 50,00")
print(f"{notas_de_20} nota(s) de R$ 20,00")
print(f"{notas_de_10} nota(s) de R$ 10,00")
print(f"{notas_de_5} nota(s) de R$ 5,00")
print(f"{notas_de_2} nota(s) de R$ 2,00")
print(f"{notas_de_1} nota(s) de R$ 1,00")