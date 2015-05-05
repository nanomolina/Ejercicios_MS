from random import random
from math import sqrt, log


def metodoComposicion():
    while True:
        y1 = -log(random())
        y2 = -log(random())
        if y2 > ((y1 - 1) ** 2) / 2.0:
            u = random()
            if u < 0.5:
                z = y1
            else:
                z = -y1
            break
    return z


def metodoPolar():
    while True:
        v1 = 2.0 * random() - 1
        v2 = 2.0 * random() - 1
        s = (v1 ** 2) + (v2 ** 2)
        if s < 1:
            x = sqrt((-2.0 * log(s)) / s) * v1
            y = sqrt((-2.0 * log(s)) / s) * v2
            break
    return x, y
