# -*- coding: utf-8 -*-
from random  import random
from math import e, factorial


def GeneratePoissonVar(lambd):
    var_random = random()
    i = 0
    p = e ** (-lambd)
    F = p
    while var_random >= F:
        p = (lambd * p) / (i + 1)
        F += p
        i += 1
    return i


def recursivePoisson(lambd, i):
    #assert(i >= 1)
    #if i == 1:
        #result = lambd
    #else:
        #result = (lambd / i) * recursivePoisson(lambd, i - 1)
    #return result
    return e**-lambd * (lambd**i) / factorial(i)


def GeneratePoissonVarBetter(lambd):
    I = int(lambd)
    F = recursivePoisson(lambd, I)
    var_random = random()
    print "RANDOM: ", var_random
    if var_random <= F:
        x = I
        while x > 1:
            p1 = recursivePoisson(lambd, x - 1)
            p2 = recursivePoisson(lambd, x)
            if p1 <= var_random <= p2:
                break
            else:
                x -= 1
    else:
        x = I + 1
        while var_random >= F:
            try:
                p1 = recursivePoisson(lambd, x)
                p2 = recursivePoisson(lambd, x + 1)
            except:
                break
            if p1 <= var_random <= p2:
                break
            else:
                F += p1
                x += 1
    return x