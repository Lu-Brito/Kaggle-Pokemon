# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:58:52 2018

@author: Lux
"""

#importações
import pandas as pd
import numpy 
import random
import matplotlib.pyplot as plt

#carrega o dataset
pokemon_dataset = pd.read_csv('/Users/lucia/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.6/pokemon.csv')

b = list (pokemon_dataset['weight_kg'])

#cria um subset do pokemon_dataset
i=0
lista = []
while i<=1000:
    i = i+1
    random.shuffle(b)
    subpokeset = b[0:100]
    soma = 0
    for weight_kg in subpokeset:
        count = 0
        if not numpy.isnan (weight_kg):
            count = count +1
            soma = soma + (weight_kg)  
    media = soma/(len(subpokeset)-count)
    lista.append (media)

bar_color = 'green'

plt.hist(lista, bins = 10, color = bar_color, rwidth = 0.85)    

plt.title ('Médias para 1000 pokeamostras de pesos')
plt.xlabel ('Pokepeso (kg)')
plt.ylabel('Frequência')
plt.show()

    
input()