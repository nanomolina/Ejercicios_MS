# -*- coding: utf-8 -*-
from random import random


def sumatory(lambd, k):
    result = 0.0
    p = 1.0
    for j in range(k):
        result += p
        p = (p * lambd) / (j + 1)
    return result


# Funcion uniforme en [0,..,10]
def g(x):
    return 1.0/(x + 1)


def f(x, lambd, k):
    result = 1.0
    p = 1.0 / sumatory(lambd, k)
    for i in range(x):
        result *= p
        p = lambd / (i + 1)
    return result


def maxP(lambd, k):
    max_val = 0.0
    for i in range(k + 1):
        div = f(i, lambd, k) / g(i)
        max_val = max(max_val, div)
    return max_val


def genPoissonVar(lambd, k):
    while True:
        var_random1 = random()
        Y = int((k + 1) * var_random1) + 1
        var_random2 = random()
        max_val = maxP(lambd, k)
        p_Y = f(Y, lambd, k)
        q_Y = g(Y)
        if var_random2 <= p_Y/(max_val * q_Y):
            result = Y
            break
    return result


