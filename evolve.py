# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:01:05 2019

@author: YS15101711
"""
from utils import initList
from population import Population


def evolve(ancestorList, numGenerations):
    """
    evolves the original population forward by numGenerations 
    """
    firstGen = Population(ancestorList)
    if numGenerations == 0:
        return firstGen
    elif numGenerations > 0:
        i = 0
        currentGen = firstGen
        while i < numGenerations:
            nextGen = Population(currentGen.getAncestors())
            currentGen = nextGen
            i += 1
    return nextGen
        
def main():

    popSize = 8
    numGen = 20
    
    initAncList = initList(popSize)
    finalGen = evolve(initAncList, numGen)
    
    print(finalGen.getAncestors()) 
    
if __name__ == '__main__':
    main()
            
        
        