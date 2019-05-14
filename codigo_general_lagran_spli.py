import matplotlib.pyplot as pl
import numpy as np
from numpy import loadtxt
from scipy.interpolate import interp1d
from scipy import linspace

class lagrange:
    def __init__(self):
        print("Clase inicializada")
    
    def interpolacion(self,xm,ym, x_interp):
        #print(xm,ym,x_interp)
        n = len(xm)
        ele = 1.
        y = 0.
        y_interp = []
        for x in range(len(x_interp)):
            #print(x_interp[x])
            y = 0.
            for j in range(len(ym)):
               
                ele = 1.
                for m in range(len(ym)):
                    if m != j:
                        #print(x_interp[x]-xm[m])
                        #print((x_interp[x]-xm[m])/(xm[j]-xm[m]))
                        ele *=(x_interp[x]-xm[m])/(xm[j]-xm[m]) 
                        
                        #print(ele)
                y += ele*ym[j]
            
            y_interp.append(y)
       
            
        #print(y_interp)
        return (y_interp)
    
    
a = loadtxt("datos.dat")
#fig = pl.figure(figsize= (4,4), dpi=100)
#pl.scatter(a[:,0],a[:,1])
#pl.title("Datos Experimentales")
#pl.xlabel("E")
#pl.ylabel("F(e)")
#pl.grid("on")

rango_interp = linspace(min(a[:,0]),max(a[:,0]),1000)

y = np.array(interp1d(a[:,0],a[:,1],kind=('cubic'))(rango_interp))

interpo = lagrange()
fun = np.array(interpo.interpolacion(a[:,0],a[:,1],rango_interp))
maximo1 = np.amax(fun)
maximo_indice1 = np.argmax(fun)
pl.plot(rango_interp,y)
pl.scatter(a[:,0],a[:,1])
pl.plot(rango_interp,fun)
pl.scatter(rango_interp[maximo_indice1], maximo1 , marker='^',facecolor ='blue',s = 80)
pl.text(rango_interp[maximo_indice1]+5, maximo1, r'$E_{r}$ = %0.4f (lagrange)'%(maximo1), fontsize=10)

maximo2 = np.amax(y)
maximo_indice2 = np.argmax(y)

pl.scatter(rango_interp[maximo_indice2], maximo2 , marker='^',facecolor ='blue',s = 80)
pl.text(rango_interp[maximo_indice2]+50, maximo2-40, r'$E_{r}$ = %0.4f (spline)'%(maximo2), fontsize=10)
indice = []
ajuste = (maximo1/2)*0.01
print(ajuste)
for i in range(len(fun)):
    if fun[i] >= (maximo1/2)-ajuste and fun[i] <= (maximo1/2)+ajuste:
        indice.append(i) 

pl.scatter(rango_interp[indice[4]], fun[indice[4]] , marker='*',facecolor ='red',s = 80)
pl.scatter(rango_interp[indice[6]], fun[indice[6]] , marker='*',facecolor ='red',s = 80)
gamma = rango_interp[indice[6]]-rango_interp[indice[4]]
pl.grid("on")
pl.text(150, 35, r'$\Gamma$ = %0.4f '%(gamma), fontsize=10)
