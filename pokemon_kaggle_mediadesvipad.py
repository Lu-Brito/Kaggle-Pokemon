# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:58:52 2018

@author: Lux
"""

#importa pandas
import pandas as pd
import numpy 

#carrega o dataset
pokemon_dataset = pd.read_csv('/Users/lucia/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.6/pokemon.csv')

#a = list (pokemon_dataset['pokedex_number'])
b = list (pokemon_dataset['weight_kg'])
#print (b)

#calcula média 
#retira nan pythonicamente ;)
b = [x for x in b if str(x)!='nan']

media = sum(b)/len(b)
print('A média dos Pokepesos é',media, 'kg')

#calcula desvpad
print('O desvio padrão dos Pokepesos é',numpy.std(b),'kg')

