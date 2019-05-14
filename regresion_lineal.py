#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 08:35:28 2019

@author: usuario
"""
import numpy as np
import matplotlib.pyplot as pl

class regresion:
    def __init__(self):
        print("")
        
    def regresion_lineal(self,x,y):
        s = 0.
        sx = 0.
        sy = 0.
        sxx = 0.
        syx = 0.
        for i in range(len(x)):
            sigma = np.sqrt(y[i])
            s += 1/(sigma**2)
            sx += x[i]/(sigma**2)
            sy += y[i]/(sigma**2)
            sxx += (x[i]**2)/(sigma**2)
            syx += x[i]*y[i]/(sigma**2)
            
        delta = (s*sxx)-(sx**2)
        a1 = (sxx*sy-sx*syx)/delta
        a2 = (s*syx-sx*sy)/delta   
        
     
        return([a1,a2])
    def regresion_depurada(self,x,y):
        xmed = 0.
        ymed = 0.
        sxy = 0.
        sxx = 0.
        for j in range(len(x)):
            xmed += x[j]
            ymed += y[j]
        xmed = xmed/len(x)
        ymed = ymed/len(x)
        for i in range(len(x)):
             sigma = np.sqrt(y[i])
             sxy += (x[j]-xmed)*(y[j]-ymed)/(sigma**2)
             sxx += ((x[j]-xmed)**2)/(sigma**2)
        
        