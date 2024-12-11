# c) Importe a biblioteca datetime e exiba a data e hora atuais.

# imporando diretamente para evitar ficar digitando demais
from datetime import datetime

data = datetime.now()

# usando a sintaxe de data e hora do unix para representar as informações
hora = data.strftime('%H:%M:%S')
data = data.strftime('%d/%m/%Y')

print(f'A data e hora atuais são: {data} {hora}')