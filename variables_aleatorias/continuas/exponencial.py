from random import random
from math import log

def genExp(lambd):
    u = random()
    return -(1.0 / lambd) * log(u)
