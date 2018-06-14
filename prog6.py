# -*- coding: utf-8 -*-
"""
nome: prog6.py
@author: auro
"""
#este programa multa o usuario de acordo com a velocidade

x = float(input("qual a sua velocidade? "))

if x > 120:
    multa = (x - 120) * 5
    print("voce foi multado! a sua multa eh de ", multa, "reais")
else:
    print("voce eh um bom motorista!")
