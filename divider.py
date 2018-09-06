#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:41:47 2018

@author: joe
"""

import pandas as pd
import numpy as np

class divider:
    
    def __init__(self, array):
        self.array = array
        self.history = []
    
    def divide(self):
        divided = False
        for a in range(len(self.array)):
            if divided:
                break
            for b in range(len(self.array) - 1):
                b += 1
                if (not a == b) and (not divided):
                    if self.array[a] % self.array[b] == 0:
                        answer = int(self.array[a] / self.array[b])
                        self.history.append('{} / {} = {}'.format(self.array[a], 
                                            self.array[b], answer))
                        self.array[a] = answer
                        self.array.remove(self.array[b])
                        divided = True
                    elif self.array[b] % self.array[a] == 0:
                        answer = int(self.array[b] / self.array[a])
                        self.history.append('{} / {} = {}'.format(self.array[b], 
                                            self.array[a], answer))
                        self.array[a] = answer
                        self.array.remove(self.array[b])
                        divided = True
                        
def adder(array, history, df, target):
    l = len(array)
    for a in range(l):
        for b in np.arange(a + 1, l):
            if not a == b:
                answer = array[a] + array[b]
                temphist = history.copy()
                temphist.append('{} + {} = {}'.format(array[a], array[b], answer))
                if answer == target:
                        print(temphist)
                temparr = array.copy()
                temparr[a] += temparr[b]
                temparr.remove(temparr[b])
                temp = pd.DataFrame({'Numbers': [], 'History': []})
                temp = temp.append({'Numbers': temparr, 'History': temphist}, ignore_index = True)
                df = df.append(temp, ignore_index = True)
    return df

def multiplier(array, history, df, target):
    l = len(array)
    for a in range(l):
        for b in np.arange(a + 1, l):
            if not a == b:
                answer = array[a] * array[b]
                temphist = history.copy()
                temphist.append('{} * {} = {}'.format(array[a], array[b], answer))
                if answer == target:
                        print(temphist)
                temparr = array.copy()
                temparr[a] *= temparr[b]
                temparr.remove(temparr[b])
                temp = pd.DataFrame({'Numbers': [], 'History': []})
                temp = temp.append({'Numbers': temparr, 'History': temphist}, ignore_index = True)
                df = df.append(temp, ignore_index = True)
    return df

def minus(array, history, df, target):
    l = len(array)
    for a in range(l):
        for b in np.arange(a + 1, l):
            if not a == b:
                temphist = history.copy()
                temparr = array.copy()
                temp = pd.DataFrame({'Numbers': [], 'History': []})
                if array[a] > array[b]:
                    answer = array[a] + array[b]
                    temphist.append('{} - {} = {}'.format(array[a], array[b], answer))
                    if answer == target:
                        print(temphist)
                    temparr[a] -= temparr[b]
                    temparr.remove(temparr[b])
                    temp = temp.append({'Numbers': temparr, 'History': temphist}, ignore_index = True)
                    df = df.append(temp, ignore_index = True)
                elif array[b] > array[a]:
                    answer = array[b] - array[a]
                    temphist.append('{} - {} = {}'.format(array[b], array[a], answer))
                    if answer == target:
                        print(temphist)
                    temparr[b] -= temparr[a]
                    temparr.remove(temparr[a])
                    temp = temp.append({'Numbers': temparr, 'History': temphist}, ignore_index = True)
                    df = df.append(temp, ignore_index = True)
    return df

def division(array, history, df, target):
    l = len(array)
    for a in range(l):
        for b in np.arange(a + 1, l):
            if not a == b:
                temphist = history.copy()
                temparr = array.copy()
                temp = pd.DataFrame({'Numbers': [], 'History': []})
                if array[a] % array[b] == 0:
                    answer = array[a] / array[b]
                    temphist.append('{} / {} = {}'.format(array[a], array[b], answer))
                    if answer == target:
                        print(temphist)
                    temparr[a] /= temparr[b]
                    temparr.remove(temparr[b])
                    temp = temp.append({'Numbers': temparr, 'History': temphist}, ignore_index = True)
                    df = df.append(temp, ignore_index = True)
                elif array[b] % array[a] == 0:
                    answer = array[b] / array[a]
                    temphist.append('{} / {} = {}'.format(array[b], array[a], answer))
                    if answer == target:
                        print(temphist)
                    temparr[b] /= temparr[a]
                    temparr.remove(temparr[a])
                    temp = temp.append({'Numbers': temparr, 'History': temphist}, ignore_index = True)
                    df = df.append(temp, ignore_index = True)
    return df
                        
df = pd.DataFrame({'Numbers': [], 'History': []})
numbers = [1, 2, 3, 4, 5, 6]
target = 125
df = df.append({'Numbers': numbers, 'History': []}, ignore_index = True)
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
    