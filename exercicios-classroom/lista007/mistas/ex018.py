def extrair_extensoes(lista_arquivos):
    extensoes = [arquivo.split('.')[-1] for arquivo in lista_arquivos if '.' in arquivo]
    return extensoes

# Exemplo de uso
arquivos = ['imagem.jpg', 'documento.pdf', 'musica.mp3', 'texto']
print(extrair_extensoes(arquivos))  # Saída: ['jpg', 'pdf', 'mp3']