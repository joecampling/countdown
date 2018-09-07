#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:41:47 2018

@author: joe
"""

import pandas as pd
import numpy as np

class divider_object:
    
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
    temparr = []
    arr_of_dfs = []
    arr_of_dfs.append(df)
    for a in range(l):
        for b in np.arange(a + 1, l):
            temphist = history.copy()
            temphist.append('{} + {} = {}'.format(array[a], array[b], array[a] + array[b]))
            if array[a] + array[b] == target:
                    print(temphist)
            temparr = array.copy()
            temparr[a] += temparr[b]
            temparr.remove(temparr[b])
            tempdf = pd.DataFrame({'Numbers': [temparr], 'History': [temphist]})
            arr_of_dfs.append(tempdf)
    
    return pd.concat(arr_of_dfs)

def adder_arr(numbers, history, numarr, histarr, target):
    l = len(numbers)
    for a in range(l):
        for b in np.arange(a + 1, l):
            temphist = history.copy()
            temphist.append('{} + {} = {}'.format(numbers[a], numbers[b], numbers[a] + numbers[b]))
            if numbers[a] + numbers[b] == target:
                    print(temphist)
            temparr = numbers.copy()
            temparr[a] += temparr[b]
            temparr.remove(temparr[b])
            numarr.append(temparr.copy())
            histarr.append(temphist.copy())
    
    return numarr, histarr

def multiplier_arr(numbers, history, numarr, histarr, target):
    l = len(numbers)
    for a in range(l):
        for b in np.arange(a + 1, l):
            temphist = history.copy()
            temphist.append('{} * {} = {}'.format(numbers[a], numbers[b], numbers[a] * numbers[b]))
            if numbers[a] * numbers[b] == target:
                    print(temphist)
            temparr = numbers.copy()
            temparr[a] *= temparr[b]
            temparr.remove(temparr[b])
            numarr.append(temparr.copy())
            histarr.append(temphist.copy())
    
    return numarr, histarr

def minus_arr(numbers, history, numarr, histarr, target):
    numbers.sort(reverse = True)
    l = len(numbers)
    for a in range(l):
        for b in np.arange(a + 1, l):
            if numbers[a] > numbers[b]:
                temphist = history.copy()
                temphist.append('{} - {} = {}'.format(numbers[a], numbers[b], numbers[a] - numbers[b]))
                if numbers[a] - numbers[b] == target:
                        print(temphist)
                temparr = numbers.copy()
                temparr[a] -= temparr[b]
                temparr.remove(temparr[b])
                numarr.append(temparr.copy())
                histarr.append(temphist.copy())
    
    return numarr, histarr

def divider_arr(numbers, history, numarr, histarr, target):
    numbers.sort(reverse = True)
    l = len(numbers)
    for a in range(l):
        for b in np.arange(a + 1, l):
            if numbers[a] % numbers[b] == 0:
                temphist = history.copy()
                temphist.append('{} / {} = {}'.format(numbers[a], numbers[b], numbers[a] / numbers[b]))
                if numbers[a] / numbers[b] == target:
                        print(temphist)
                temparr = numbers.copy()
                temparr[a] /= temparr[b]
                temparr.remove(temparr[b])
                numarr.append(temparr.copy())
                histarr.append(temphist.copy())
    
    return numarr, histarr

def multiplier(array, history, df, target):
    l = len(array)
    temparr = []
    arr_of_dfs = []
    arr_of_dfs.append(df)
    for a in range(l):
        for b in np.arange(a + 1, l):
            temphist = history.copy()
            temphist.append('{} * {} = {}'.format(array[a], array[b], array[a] * array[b]))
            if array[a] * array[b] == target:
                    print(temphist)
            temparr = array.copy()
            temparr[a] *= temparr[b]
            temparr.remove(temparr[b])
            tempdf = pd.DataFrame({'Numbers': [temparr], 'History': [temphist]})
            arr_of_dfs.append(tempdf)
    
    return pd.concat(arr_of_dfs)

def multiplier2(array, history, df, target):
    l = len(array)
    for a in range(l):
        for b in np.arange(a + 1, l):
            answer = array[a] * array[b]
            temphist = history.copy()
            temphist.append('{} * {} = {}'.format(array[a], array[b], answer))
            if answer == target:
                    print(temphist)
            temparr = np.copy(array)
            temparr[a] *= temparr[b]
            np.delete(temparr, b)
            df = df.append({'Numbers': temparr, 'History': temphist}, ignore_index = True)
    return df

def minus(array, history, df, target):
    array.sort(reverse = True)
    l = len(array)
    temparr = []
    arr_of_dfs = []
    arr_of_dfs.append(df)
    for a in range(l):
        for b in np.arange(a + 1, l):
            if array[a] > array[b]:
                temphist = history.copy()
                temphist.append('{} - {} = {}'.format(array[a], array[b], array[a] - array[b]))
                if array[a] - array[b] == target:
                        print(temphist)
                temparr = array.copy()
                temparr[a] -= temparr[b]
                temparr.remove(temparr[b])
                tempdf = pd.DataFrame({'Numbers': [temparr], 'History': [temphist]})
                arr_of_dfs.append(tempdf)
    
    return pd.concat(arr_of_dfs)

def minus2(array, history, df, target):
    array.sort(reverse = True)
    l = len(array)
    for a in range(l):
        for b in np.arange(a + 1, l):
            temphist = history.copy()
            temparr = np.copy(array)
            if array[a] > array[b]:
                answer = array[a] - array[b]
                temphist.append('{} - {} = {}'.format(array[a], array[b], answer))
                if answer == target:
                    print(temphist)
                temparr[a] -= temparr[b]
                np.delete(temparr, b)
                df = df.append({'Numbers': temparr, 'History': temphist}, ignore_index = True)
    return df

def division(array, history, df, target):
    array.sort(reverse = True)
    l = len(array)
    temparr = []
    arr_of_dfs = []
    arr_of_dfs.append(df)
    for a in range(l):
        for b in np.arange(a + 1, l):
            if array[a] % array[b] == 0:
                temphist = history.copy()
                temphist.append('{} / {} = {}'.format(array[a], array[b], array[a] / array[b]))
                if array[a] / array[b] == target:
                        print(temphist)
                temparr = array.copy()
                temparr[a] /= temparr[b]
                temparr.remove(temparr[b])
                tempdf = pd.DataFrame({'Numbers': [temparr], 'History': [temphist]})
                arr_of_dfs.append(tempdf)
    
    return pd.concat(arr_of_dfs)

def division2(array, history, df, target):
    array = np.flipud(np.sort(array))
    l = len(array)
    for a in range(l):
        for b in np.arange(a + 1, l):
            temphist = history.copy()
            temparr = np.copy(array)
            if array[a] % array[b] == 0:
                answer = array[a] / array[b]
                temphist.append('{} / {} = {}'.format(array[a], array[b], answer))
                if answer == target:
                    print(temphist)
                temparr[a] /= temparr[b]
                np.delete(temparr, b)
                df = df.append({'Numbers': temparr, 'History': temphist}, ignore_index = True)
    return df