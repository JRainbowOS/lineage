# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:02:13 2019

@author: YS15101711
"""
import numpy as np

def initList(populationSize):
    assert populationSize % 2 == 0, 'Make population size even!'
    result = [[i, [i]] for i in range(populationSize)]
    return result

def initArray(populationSize):
    assert populationSize % 2 == 0, 'Make population size even!'
    result = np.array([np.array([i, np.array([i, 0])]) for i in range(populationSize)])
    return result
    
def initDict(populationSize):
    assert populationSize % 2 == 0, 'Make population size even!'
    result = [{i: i} for i in range(populationSize)]
    return result
