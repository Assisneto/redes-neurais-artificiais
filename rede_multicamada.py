# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:07:18 2017

@author: Assisneto Damasceno
"""

import numpy as np

def sigmoid(soma):
    return 1/(1+ np.exp(-soma))

entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1],])

saidas = np.array([[0],[1],[1],[0]])

peso0 = np.array([[-0.424,-0.740,-0.961],
                  [0.358, -0.577, -0.469]])

pesos1 = np.array([[-0.017],[-0.893],[0.148]])

epocas = 100

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, peso0)
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)