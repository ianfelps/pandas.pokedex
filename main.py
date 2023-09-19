from IPython.display import display
import pandas as pd
import random
import os

# importar o dataframe
print(' ')
pokedex_df = pd.read_csv("pokemon.csv")

# exibir o data frame
print(' ')
print('----- Pokédex ' + 80*'-')
display(pokedex_df)

# exibir somente o topo
print(' ')
print('----- Pokédex Iniciais ' + 80*'-')
display(pokedex_df.head(16))

# exibir descrição do dataframe
print(' ')
print('----- Estatísticas Pokédex ' + 80*'-')
display(pokedex_df.describe())

# exibir somente colunas expecificas
print(' ')
print('----- Pokédex Nome e Tipo ' + 80*'-')
nome_tipo = pokedex_df[['Name', 'Type1', 'Type2']]
display(nome_tipo)

# pegar uma linha
print(' ')
print('----- Pokédex Bulbasaur ' + 80*'-')
display(pokedex_df.loc[0:4])

# pegar linhas a partir de uma condição
print(' ')
print('----- Pokédex Água ' + 80*'-')
display(pokedex_df.loc[pokedex_df['Type1'] == 'Water'])

# pegar várias linhas e colunas (nao todas)
print(' ')
print('----- Pokédex Lendários ' + 80*'-')
lendarios = pokedex_df.loc[pokedex_df['Legendary'] == True, ['Name', 'Generation', 'Legendary']]
display(lendarios)

# pegar um valor especifico
print(' ')
print('----- Pokémon ' + 80*'-')
print(pokedex_df.loc[0, 'Name'])

# calcular indicadores
print(' ')
print('----- Pokédex Tipos Primários ' + 80*'-')
display(pokedex_df['Type1'].value_counts())

print(' ')
print('----- Pokédex Média dos Tipos ' + 80*'-')
display(pokedex_df[['Type1', 'Total', 'HP', 'Attack', 'Defense', 'Sp_Attack', 'Sp_Defense', 'Speed']].groupby('Type1').mean())

# sortear linha
print(' ')
print('----- Estou com Sorte! ' + 80*'-')
display(pokedex_df.sample())

print(' ')