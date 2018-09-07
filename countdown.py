# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:18:20 2018

@author: freer
"""
import pandas as pd
import numpy as np

from functions import adder, multiplier, division, minus, adder_arr, minus_arr, multiplier_arr, divider_arr
print('Input starting numbers:')
a = int(input('First: '))
b = int(input('Second: '))
c = int(input('Third: '))
d = int(input('Fourth: '))
e = int(input('Fifth: '))
f = int(input('Sixth: '))
target = int(input('Target: '))
df = pd.DataFrame({'Numbers': [], 'History': []})
numbers = [[a, b, c, d, e, f]]
history = [[]]
#target = 940
df = df.append({'Numbers': numbers, 'History': []}, ignore_index = True)
print('Numbers:', numbers[0])
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