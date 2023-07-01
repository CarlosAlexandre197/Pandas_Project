'''Testando uma aplicação utilizando o Pandas'''

import pandas as pd
import requests

df = pd.read_excel('C:\Users\casas bahia\Desktop\Estudos\Planilha_Eu_Entrego.xlsm')

url = 'https://sgi.e-boticario.com.br/Paginas/Inicializacao/AguardarAcao.aspx'
response = requests.post(url, data=df.to_json())

if response.status_code == 200:
    print('Dados enviados com sucesso!')
else:
    print('Falha ao enviar os dados.')
