from random import random


def genBinomial(n, p):
    u = random()
    i = 0
    c = p / (1 - p)
    pr = (1 - p) ** n
    F = pr
    while u >= F:
        pr *= c * (n - i) / (i + 1)
        F += pr
        i += 1
    return i
