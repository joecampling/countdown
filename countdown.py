# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:18:20 2018

@author: freer
"""
import pandas as pd
import numpy as np

from functions import adder, multiplier, division, minus, adder_arr, minus_arr, multiplier_arr, divider_arr

df = pd.DataFrame({'Numbers': [], 'History': []})
numbers = [[1, 2, 3, 4, 5, 6]]
history = [[]]
target = 125
df = df.append({'Numbers': numbers, 'History': []}, ignore_index = True)
print('Numbers:', numbers)
print('Target:', target)
processing = True
i = 0

while processing:
    try:
        numbers[i]
    except:
        break
    numbers, history = adder_arr(numbers[i], history[i], numbers, history, target)
    numbers, history = multiplier_arr(numbers[i], history[i], numbers, history, target)
    numbers, history = minus_arr(numbers[i], history[i], numbers, history, target)
    numbers, history = divider_arr(numbers[i], history[i], numbers, history, target)
    i += 1
    
'''    

while processing:

    df = adder(df['Numbers'].iloc[i], df['History'].iloc[i], df, target)
    df = multiplier(df['Numbers'].iloc[i], df['History'].iloc[i], df, target)
    df = minus(df['Numbers'].iloc[i], df['History'].iloc[i], df, target)
    df = division(df['Numbers'].iloc[i], df['History'].iloc[i], df, target)
    i += 1
'''