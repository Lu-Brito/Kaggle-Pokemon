# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:58:52 2018

@author: Lux
"""

#importa pandas
import pandas as pd

#carrega o dataset
pokemon_dataset = pd.read_csv('/Users/lucia/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.6/pokemon.csv')

#imprime o dataset
#print(pokemon_dataset)#.loc[pokemon_dataset.index.map('pokedex_number')])
#pokemon_dataset.sort_index(5)

a = list (pokemon_dataset['pokedex_number'])
b = list (pokemon_dataset['weight_kg'].sort_values())

#print (a)
#print(b)

#importa matplotlib
import matplotlib.pyplot
from matplotlib import pyplot as plt

plt.title ('Poke Pesos XD')
plt.xlabel ('pokedex_number')
plt.ylabel('weight_kg')

#plota um gráfico de dispersão com o dataset
matplotlib.pyplot.scatter(a,b, color = 'magenta')
plt.show()

input()
