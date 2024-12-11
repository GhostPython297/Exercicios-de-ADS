# f) Escreva um programa que use a biblioteca csv para ler um arquivo CSV e exibir seu
# conteúdo.

import csv

# Nome do arquivo CSV a ser lido como exemplo
nome_arquivo = 'exercicios-classroom/lista007/bibliotecas/aaa.csv'

# Abrindo o arquivo CSV
# Abre o arquivo CSV no modo de leitura ('r')
# newline='' é usado para evitar problemas com linhas em branco no arquivo CSV
# with statement garante que o arquivo seja fechado corretamente após sua leitura, mesmo que ocorra algum erro durante o processo.
# encoding='latin-1' é usado para lidar com caracteres especiais no arquivo CSV
with open(nome_arquivo, mode='r', encoding='latin-1', newline='') as arquivo_csv:
    # Criando um objeto leitor CSV
    # O objeto leitor CSV é usado para ler o conteúdo do arquivo CSV.
    # Esse leitor lê cada linha do CSV como uma lista de strings, onde cada string representa um campo (ou célula) da linha do CSV.
    leitor_csv = csv.reader(arquivo_csv)

    # Iterando pelas linhas do arquivo CSV e exibindo o conteúdo
    # o for percorre cada linha do arquivo
    for linha in leitor_csv:
        # concatena os elementos da lista 'linha' em uma única string
        # separa por vírgulas e espaços
        # formando uma string
        print(', '.join(linha)) 
