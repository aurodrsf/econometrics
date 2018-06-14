# -*- coding: utf-8 -*-
"""
nome: prog4.py
@author: auro
"""

# este programa calcula as raizes de um polinomio de segundo grau

import numpy as np

x = float(input("digite o primeiro coeficiente: "))
y = float(input("digite o segundo coeficiente: " ))
z = float(input("digite o ultimo coeficiente: "))

#calculo das raizes
coeff = [x, y, z]
print("as raizes deste polinomio sao:", np.roots(coeff))