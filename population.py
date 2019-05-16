# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:48:00 2019

@author: YS15101711
"""
import numpy as np
from numpy.random import permutation
from random import shuffle, randint

class Population:
    
    def __init__(self, ancestorList):
        self.ancestorList = ancestorList
        self.partners = self.findPartners()
        self.children = self.getChildren()
        
    def findPartners(self):
        """
        returns a random array of odd/even partner combinations
        """
        perm = list(2 * permutation(np.arange(len(self.ancestorList) / 2)) + 1)
        partners = [[2 * i, int(perm[i])] for i in range(int(len(self.ancestorList) / 2))]
        shuffle(partners)
        return partners
    
    def getChildren(self):
        """
        returns a list of children with random parents assigned to each child
        """
        part = self.partners
        children = []
        numChildren = int(len(self.ancestorList))
        for i in range(numChildren):
            rand = randint(0, numChildren / 2 - 1)
            children.append([i, part[rand]])
        return children
                
    def getAncestors(self):
        """
        returns the list of members of the original generation which are related to
        each member of the current generation
        """
        anc = self.ancestorList
        chi = self.children
        ancestors = []
        for c in chi:
            newanc = []
            for p in c[1]:
                newanc.append(anc[p][1])
                deduped = list(set([item for sublist in newanc for item in sublist]))
            ancestors.append([c[0], deduped])
        return ancestors
