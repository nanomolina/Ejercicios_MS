from random import random
from math import e, log


def genPoissonNormal(lambd):
    u = random()
    i = 0
    while not u < e ** -lambd:
        i += 1
        u *= random()
    return i


def poissonHomogeno(lambd, T):
    t = 0.0
    s = []
    while True:
        u = random()
        if t - (1.0 / lambd) * log(u) > T:
            break
        else:
            t += -(1.0 / lambd) * log(u)
            s.append(t)
    return s


# Algoritmo de Adelgazamiento
def poissonNoHomogeneo1(lambd, T, fun_lambd):
    t = 0
    s = []
    while True:
        u = random()
        if t - (1 / lambd) * log(u) > T:
            break
        else:
            t += -(1 / lambd) * log(u)
            v = random()
            if v < fun_lambd(t) / lambd:
                s.append(t)
    return s

