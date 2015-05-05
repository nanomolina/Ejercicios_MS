from random import random
from math import log


def genGamma(n, lambd):
    u = 1.0
    for _ in range(n):
        u *= random()
    return -(1.0 / lambd) * log(u)
