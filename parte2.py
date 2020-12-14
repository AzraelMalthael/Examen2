# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:30:24 2020

@author: Windows Vista
"""
V = 4
resp = [] 
import numpy as np
import pandas as pd
dato=pd.read_csv("datos2.csv")
aux=np.array(dato)
def tsp(grafo, v, pos, n, cont, costo): 
    print(costo, pos, n, cont)
    if (cont == n and grafo[pos][0]>0): 
        print("nueva iteracion")
        print((costo + grafo[pos][0]))
        resp.append(costo + grafo[pos][0]) 
        return
    for i in range(n): 
        if (v[i] == False and grafo[pos][i]>0): 
            v[i] = True
            tsp(grafo, v, i, n, cont + 1, costo + grafo[pos][i]) 
            v[i] = False
if __name__ == '__main__': 
    n = 4
    grafo= aux
    v = [False for i in range(n)]     
    v[0] = True
    tsp(grafo, v, 0, n, 1, 0) 
    print(min(resp)) 

  