#!/usr/bin/env python
# coding: utf-8

# ## Análise Exploratória de Dados em Linguagem Python Para a Área de Varejo

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# In[ ]:


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# ## Carregando os dados

# In[ ]:


# Carregando o dataset através da função 'read_csv()' do  Pandas

dados = pd.read_csv('dados/dataset.csv')


# In[ ]:


# Verificando a dimensão dos dados

dados.shape


# 9700 linhas e 11 colunas

# In[ ]:


# Amostra das 5 primeiras linhas da tabela

dados.head()


# In[ ]:


# Amostra das 5 últimas linhas da tabela

dados.tail()


# ## Análise Exploratória

# In[ ]:


# Verificando as colunas do conjuto de dados

dados.columns


# In[ ]:


# Verificando o tipo de dado de cada coluna

dados.dtypes


# In[ ]:


# Resuo estatístico da coluna com o valor de venda

dados['Valor_Venda'].describe()


# In[ ]:


# Verificando dados duplicados

dados[dados.duplicated()]


# In[ ]:


# Verificando se há valores ausentes

dados.isnull().sum()


# ## Perguntas de Negócio

# ### 1. Qual a cidade com maior Valor de Venda de produtos da categoria 'Office Supplies'?

# In[ ]:


# filtrando os dados pela categoria
dados_p1 = dados[dados['Categoria'] == 'Office Supplies']


# In[ ]:


# soma do total de vendas agrupado por cidade
dados_p1_total = dados_p1.groupby('Cidade')['Valor_Venda'].sum()


# In[ ]:


# selecionando a cidade com maior valor de venda através da função 'idxmax()'
maior_venda = dados_p1_total.idxmax()
print("Cidade com maior valor de venda para 'Office Supplies':", maior_venda)


# In[ ]:


# Conferindo o resultado, consultando a soma do valor_vendas de cada cidade - descendente

dados_p1_total.sort_values(ascending = False)


# ### 2. Qual o total de vendas por data do pedido?

# In[ ]:


# Soma do total de vendas agrupado por 'data_pedido'
dados_p2 = dados.groupby('Data_Pedido')['Valor_Venda'].sum()


# In[ ]:


# Visualizando as 5 primeiras linhas
dados_p2.head()


# In[ ]:


# Gráfico de barras a partir do próprio DataFrame
#dimensão da imagem
#eixos e cor
#título do gráfico
#visualização do gráfico


# In[ ]:


plt.figure(figsize=(20,6)) 
dados_p2.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'green') 
plt.title('Total de Vendas por Data do Pedido')
plt.show()


# ### 3. Qual o total de vendas por estado

# In[ ]:


# Soma das vendas agrupado por Estado
dados_p3 = dados.groupby('Estado')['Valor_Venda'].sum().reset_index()


# A função **reset_index()** no seu código é utilizada para transformar o índice (que é o 'Estado' no seu caso) de volta em uma coluna do DataFrame. Isso é necessário para que, ao criar um gráfico de barras com Seaborn, você possa referenciar essa coluna como a variável no eixo x. Se não usar reset_index(), o índice da série seria considerado como o eixo x, o que pode levar a resultados inesperados ou erros. Portanto, o uso de reset_index() é crucial para garantir a correta representação dos dados no gráfico.

# In[ ]:


# Visualização das 5 primeiras linhas 
dados_p3.head()


# In[ ]:


# Gráfico de barras com seaborn(barplot)

plt.figure(figsize = (16,6))
sns.barplot(data = dados_p3,
           y = 'Valor_Venda',
           x = 'Estado').set(title = 'Vendas Por Estado')
plt.xticks(rotation = 80) #rotacionado para melhor visibilidade
plt.show()


# ### 4. Quais são as 10 cidades com maior total de vendas?

# In[ ]:


# Soma do Valor de Venda agrupado por cidade
# dados_p4 = dados.groupby('Cidade')['Valor_Venda'].sum()


# In[ ]:


# Transformando a 'série Cidade' em 'coluna cidade' novamente
#.reset_index()


# In[ ]:


# Ordenado os valores da coluna 'valor_venda' em ordem decrescente de delimitando aos 10 primeiros
#.sort_values(by = 'Valor_Venda', ascending = False).head(10)


# In[ ]:


dados_p4 = dados.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = False).head(10)


# In[ ]:


dados_p4


# In[ ]:


# Gráfico de barras com seaborn(barplot)

plt.figure(figsize = (16,6))
sns.set_palette('coolwarm') #especificar a paleta de cores da barra
sns.barplot(data = dados_p4,
           y = 'Valor_Venda',
           x = 'Cidade').set(title = 'As 10 Cidades com Maior Valor de Venda')
plt.xticks(rotation = 80) #rotacionado para melhor visibilidade
plt.show()


# ### 5. Qual o segmento teve o maior total de vendas?

# In[ ]:


dados_p5 = dados.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = False)


# In[ ]:


dados_p5


# In[ ]:


# função para converter os dados que estão em notação cientifica para valor absoluto

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '$ {v:d}'.format(v=val)
    return my_format


# In[ ]:


# Gráfico de pizza com matplotlib

plt.figure(figsize = (16,6))
plt.pie(dados_p5['Valor_Venda'],
        labels = dados_p5['Segmento'],
        autopct = autopct_format(dados_p5['Valor_Venda']),
        startangle = 90)
plt.title('As 10 Cidades com Maior Valor de Venda')
plt.show()


# In[ ]:


# Gráfico de barras com seaborn(barplot)

plt.figure(figsize = (16,6))
plt.pie(dados_p5['Valor_Venda'],
        labels = dados_p5['Segmento'],
        autopct = '%1.1f%%', #valor em porcentagem
        startangle = 90)
plt.title('As 10 Cidades com Maior Valor de Venda')
plt.show()


# In[ ]:


# Gráfico de disco com matplotlib

plt.figure(figsize = (16,6))
plt.pie(dados_p5['Valor_Venda'],
        labels = dados_p5['Segmento'],
        autopct = autopct_format(dados_p5['Valor_Venda']),
        startangle = 90)

centre_circle = plt.Circle((0,0), 0.82, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('As 10 Cidades com Maior Valor de Venda')
plt.show()


# ### 6. Qual o total de vendas por segmento e por ano?

# In[ ]:


# Converção da coluna 'data_pedido' que está no tipo object para data com a função datetime()
dados['Data_Pedido'] = pd.to_datetime(dados['Data_Pedido'], dayfirst = True)


# In[ ]:


dados.dtypes


# In[ ]:


# "extrair" o ano e armazenar em uma nova coluna - dt.year
dados['Ano'] = dados['Data_Pedido'].dt.year


# In[ ]:


# Verificando a nova coluna
dados.head()


# In[ ]:


dados_p6 = dados.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()


# In[ ]:


dados_p6


# ### 7. Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
# 
# * Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# 
# * Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
# 
# **Quantas vendas receberiam 15% de desconto?**

# In[ ]:


# numpy c/ pandas para criar condicional
# criar nova coluna para valor do desconto

dados['Desconto'] = np.where(dados['Valor_Venda'] > 1000, 0.15, 0.10)


# In[ ]:


dados.head(15)


# In[ ]:


dados['Desconto'].value_counts()


# ### 8. Considere que a empresa decida conceder o desconto de 15%, como apresentado na questão anterior. Qual seria a média do 'valor_venda' dessas vendas antes e depois do desconto?

# In[ ]:


# Sendo o desconto de 15%, o 'valor_venda' passa a ser 85% do valor

dados['Valor_Venda_Desconto'] = dados['Valor_Venda'] - (dados['Valor_Venda'] * dados['Desconto'])


# In[ ]:


dados.head(15)


# In[ ]:


# Localizar 'valor_venda' que receberiam 15% - antes do desconto
dados_vendas_antes = dados.loc[dados['Desconto'] == 0.15, 'Valor_Venda']
dados_media_antes = round(dados_vendas_antes.mean(), 2)
dados_media_antes


# In[ ]:


# Localizar 'valor_venda' que receberiam 15% - depois do desconto
dados_vendas_depois = dados.loc[dados['Desconto'] == 0.15, 'Valor_Venda_Desconto']
dados_media_depois = round(dados_vendas_depois.mean(), 2)
dados_media_depois


# ### 9. Qual o média de vendas por Segmento, Ano e Mês?

# In[ ]:


# "extrair" o mês e armazenar em uma nova coluna - dt.year
dados['Mes'] = dados['Data_Pedido'].dt.month


# In[ ]:


dados.head()


# In[ ]:


dados_p9 = dados.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].mean()


# In[ ]:


dados_p9


# In[ ]:


# Vamos extrair os níveis da variaveis categóricas
anos = dados_p9.index.get_level_values(0)
meses = dados_p9.index.get_level_values(1)
segmentos = dados_p9.index.get_level_values(2)


# In[ ]:


# Plot
# relplot - grafico relacional
plt.figure(figsize = (12, 6))
sns.set()
fig1 = sns.relplot(kind = 'line',
                   data = dados_p9, 
                   y = dados_p9, 
                   x = meses,
                   hue = segmentos, 
                   col = anos,
                   col_wrap = 4)
plt.show()


# ### 10. Qual o total de vendas por Categoria e SubCategoria, considerando somente as Top 12 SubCategorias? 
# 
# Demonstre tudo através de um único gráfico.

# In[ ]:


dados_p10 = dados.groupby(['Categoria',
                             'SubCategoria']).sum(numeric_only = True).sort_values('Valor_Venda',
                                                                                   ascending = False).head(12)


# In[ ]:


dados_p10


# In[ ]:


# Convertemos a coluna Valor_Venda em número inteiro e classificamos por categoria

dados_p10 = dados_p10[['Valor_Venda']].astype(int).sort_values(by = 'Categoria').reset_index()


# In[ ]:


# Dataframe com categorias e subcategorias
dados_p10


# In[ ]:


# Criamos outro dataframe somente com os totais por categoria
dados_p10_cat = dados_p10.groupby('Categoria').sum(numeric_only = True).reset_index()


# In[ ]:


# Listas de cores para categorias
cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']


# In[ ]:


# Listas de cores para subcategorias
cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']


# In[ ]:


# Plot

# Tamanho da figura
fig, ax = plt.subplots(figsize = (18,12))

# Gráfico das categorias
p1 = ax.pie(dados_p10_cat['Valor_Venda'], 
            radius = 1,
            labels = dados_p10_cat['Categoria'],
            wedgeprops = dict(edgecolor = 'white'), #divisão entre categorias
            colors = cores_categorias) # definidas acima

# Gráfico das subcategorias
p2 = ax.pie(dados_p10['Valor_Venda'],
            radius = 0.9,
            labels = dados_p10['SubCategoria'],
            autopct = autopct_format(dados_p10['Valor_Venda']), #formatação dos dados
            colors = cores_subcategorias, #definidas acima
            labeldistance = 0.7, 
            wedgeprops = dict(edgecolor = 'white'), #divisão entre as subcategorias
            pctdistance = 0.53,
            rotatelabels = True) #rotação dos rotulos

# Limpa o centro do círculo
centre_circle = plt.Circle((0, 0), 0.6, fc = 'white')

# Labels e anotações
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
#plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(df_dsa_p10['Valor_Venda']))), xy = (-0.2, 0))
plt.title('Total de Vendas Por Categoria e Top 12 SubCategorias')
plt.show()


# In[ ]:




