# -*- coding: utf-8 -*-
from random import random
from math import e


#version ineficiente
#def sumatory2(lambd, k):
    #total = 0.0
    #for j in range(k + 1):
        #total += ((lambd ** j) * (e ** -lambd)) / factorial(j)
    #return total


def sumatory(lambd, k):
    total = 0.0
    p = e ** -lambd
    for j in range(k):
        total += p
        p = (lambd * p) / (j + 1)
    total += p
    return total


def genPoissonVar(lambd, k):
    var_random = random()
    i = 0
    p = (e ** -lambd) / sumatory(lambd, k)
    F = p
    while var_random >= F:
        p = (lambd * p) / (i + 1)
        F += p
        i += 1
    return i