# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:18:20 2018

@author: freer
"""
import pandas as pd
import numpy as np

from functions import adder, multiplier, division, minus


print('err, hellooo?....')
df = pd.DataFrame({'Numbers': [], 'History': []})
numbers = [1, 2, 3, 4, 5, 6]
target = 125
df = df.append({'Numbers': np.sort(numbers), 'History': []}, ignore_index = True)
print('Numbers:', numbers)
print('Target:', target)
processing = True
i = 0
while processing:
    try:
        df.iloc[i]
    except:
        processing = False
        break
    df = adder(df['Numbers'].iloc[i], df['History'].iloc[i], df, target)
    df = multiplier(df['Numbers'].iloc[i], df['History'].iloc[i], df, target)
    df = minus(df['Numbers'].iloc[i], df['History'].iloc[i], df, target)
    df = division(df['Numbers'].iloc[i], df['History'].iloc[i], df, target)
    i += 1
    