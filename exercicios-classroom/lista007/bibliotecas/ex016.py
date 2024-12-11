# d) Utilize a biblioteca os para listar todos os arquivos e pastas no diretório atual.

import os

# listando os diretórios
arquivos = os.listdir('.')

# exibindo as informações do diretório raiz
for item in arquivos:
    print(item)
