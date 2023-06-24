import pandas as pd
import requests

df = pd.read_excel('caminho/para/o/arquivo.xlsx')

url = 'https://sgi.e-boticario.com.br/Paginas/Inicializacao/AguardarAcao.aspx'
response = requests.post(url, data=df.to_json())

if response.status_code == 200:
    print('Dados enviados com sucesso!')
else:
    print('Falha ao enviar os dados.')



