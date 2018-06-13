# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:58:52 2018

@author: Lux
"""

import pandas as pd


pokemon_dataset = pd.read_csv('/Users/lucia/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.6/pokemon.csv')

print(pokemon_dataset.head())

input ("Aperte <enter> para sair")