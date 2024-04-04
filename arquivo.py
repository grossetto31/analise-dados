#%%
import pandas as pd
#importar biblioteca para criação de gráficos
import plotly.express as px

#%%
#realiza a leitura do arquivo csv no google drive -> encoding="latin1" -> resolve erro utf8
tabela = pd.read_csv("ClientesBanco.csv", encoding="latin1")

#remove a coluna clientiunum
tabela = tabela.drop("CLIENTNUM",axis=1)

#mostra a tabela
print(tabela)

#%%
#exclui todas as linhas que pelo menos um valor é vazio
tabela = tabela.dropna()

#mostra informações da tabela
print(tabela.info())

#criar descrição estatistica dos dados
print(tabela.describe().round(1))

#%%
#analisar divisao de clientes x cancelados
qtd_categoria = tabela["Categoria"].value_counts()
print(qtd_categoria)
qtd_categoria_perc = tabela["Categoria"].value_counts(normalize=True).round(2)
print(qtd_categoria_perc)

#%%
#criar varios graficos para cada coluna
for coluna in tabela:
  #criar gráfico histograma para comparar categoria (cliente x cancelado) por idade
  grafico = px.histogram(tabela, x=coluna, color="Categoria")
  grafico.show()

#%%
#Aparentemente quanto mais produtos contratados -> menor a taxa de cancelamento
#Quanto mais transações e os valores das transações -> menor a chance de cancelar
#Quanto maior o número de contatos maior a chance de cancelar
