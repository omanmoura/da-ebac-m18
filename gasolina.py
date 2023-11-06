# código de geração do gráfico 

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gasolina.csv')

grafico = sns.lineplot(data=data, x='dia', y='venda')
grafico.set(title='Preço da gasolina em SP por dia', xlabel='Dia do mês', ylabel='Preço em reais')
plt.savefig('gasolina.png')