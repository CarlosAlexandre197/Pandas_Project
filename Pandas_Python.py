import pandas as pd

dataframe = pd.DataFrame()

vendas = {'data': ['26/05/2023', '27/05/2023'],
          'valor': [500, 300],
          'produto': ['malbec', 'lily'],
          'quantidade': [50, 70],
          }
vendas_df = pd.DataFrame(vendas)

print(vendas)

