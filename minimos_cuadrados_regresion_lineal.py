#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 08:16:01 2019

@author: usuario
"""

import numpy as np
import matplotlib.pyplot as pl
from sklearn.linear_model import LinearRegression
from regresion_lineal import regresion
from time import time

###implementacion con libreria 

x1 = 1e-9*np.array([5,15,25,35, 45,55,65,75,85,95, 105,115])
x = x1.reshape((-1, 1))
y = np.array([32, 17,21,7.5,8, 7, 5, 2, 4, 3,4,  1.5])
yy =np.log(y)
modelo = LinearRegression()
tiempo1_ini = time()
modelo.fit(x, yy)
modelo = LinearRegression().fit(x, yy)
tiempo1_fin = time()
total = tiempo1_fin-tiempo1_ini
r_sq = modelo.score(x, yy)

print('Chi cuadrado:', r_sq)
print('intercepto:', modelo.intercept_) ###intercepto eje y 
print('Pendiente:', modelo.coef_) ### pendiente del modelo
print("Tiempo de ejecución = ",total)
f = np.linspace(np.amin(x),np.amax(x),100)
reg = modelo.coef_*f+modelo.intercept_
pl.scatter(x,yy)
pl.plot(f,reg)

pl.title("Regresión Lineal")
pl.xlabel("Tiempo")
pl.ylabel("N(t)")

reg = regresion()
tiempo2_ini = time()
regresion_lineal = reg.regresion_lineal(x1,np.log(y))
tiempo2_fin = time()
total2 = tiempo2_fin-tiempo2_ini
reg_prop = regresion_lineal[1]*f+regresion_lineal[0]
tau = -1/regresion_lineal[1]

pl.plot(f,reg_prop)
pl.xlim([np.amin(x1),np.amax(x1)])
pl.show()
print("Mi modelo =",tau)
print("Python =",1/modelo.coef_)
print("Tiempo ejecucion propio = ", total2)
####
xi = 0.
for i in range(len(x1)):
    sigma = np.sqrt(yy[i])
    xi += ((yy[i]-reg_prop[i])/(sigma))**2
print("chi =", xi)



