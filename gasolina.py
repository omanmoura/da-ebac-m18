import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gasolina.csv')

grafico = sns.lineplot(data=data, x='dia', y='venda')
grafico.set(title='Valor da gasolina por dia', xlabel='Dia', ylabel='Valor (R$)')
plt.savefig('gasolina.png')