# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:21:59 2015

@author: Askerin
"""


import numpy as np
#import scipy as sp



class ActFunction:
    def __init__(self):
        pass
    
    def sigmoid(value):
        retVal = (1/1(1+np.exp(-value)))
        return retVal

    def sigmoidDeriv(value):
        retval = ActFunction.sigmoid(value);
        retval = np.multiply(retval, 1-retval)
        return retval    
    

    def ReLU(value):
        copy= np.copy(value)
        copy[copy<0] = 0
        return copy


    def ReLUDeriv(value):
        copy= (1/1(1+np.exp(-value)))
        return copy
        
    def LReLUDeriv(value):#Lrelu is p much still the same, so only deriv changes
        copy= np.copy(value)
        copy[copy<0] = 0
        return copy   

class Node:
    nodeVal = 0
    threshhold = 0
    
    def __init__(self):
        self.nodeVal = 0;
        self.threshhold = 1;
    
    def setVal(self,val):
        self.nodeVal = val
    
    def setThresh(self,thresh):
        self.threshold = thresh
        
        
    
class Layer:
    nodeArray = []
        
    def __init__(self, nodeNum):
        while (nodeNum!=1):
            self.nodeArray.append(Node())
            nodeNum-=1
    
    def connect():
        pass

class Network:
    
    def FFNet():
        pass
    
    def ConvNet():
        pass
    
    def RecurrentNet():
        pass
    
    def DeepNet():
        pass

    