# -*- coding: utf-8 -*-
"""
nome: prog3.py
@author: auro
"""

#este programa multa o usuario de acordo com a velocidade

x = float(input("Qual a sua velocidade? "))

#condicao da multa

if x > 80:
    multa = (x - 80) * 5
    print("voce foi multado em: ", multa, "reais")
else :
        print("voce eh um bom motorista!")
