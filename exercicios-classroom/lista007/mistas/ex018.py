# essa função serve para extrair as extensões de uma lista de arquivos
# ela recebe uma lista de arquivos e retorna uma lista de extensões
# a variável extensoes é uma lista vazia que será preenchida com as extensões
# arquivo.split() separa o nome do arquivo em uma lista de strings
# arquivo.split('.')[-1] retorna a última string da lista, que é a extensão do arquivo
# o loop for percorre a lista de arquivos e adiciona as extensões à lista de extensoes
def extrair_extensoes(lista_arquivos):
    extensoes = [arquivo.split('.')[-1] for arquivo in lista_arquivos if '.' in arquivo]
    return extensoes

# Exemplo de uso
arquivos = ['imagem.jpg', 'documento.pdf', 'musica.mp3', 'texto']
print(extrair_extensoes(arquivos))  # Saída: ['jpg', 'pdf', 'mp3']