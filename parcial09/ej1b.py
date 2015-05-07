# -*- coding: utf-8 -*-
from random import random


def moneda():
    caras = 0
    secas = 0
    lanzamientos = 0
    while abs(caras - secas) != 3:
        var_random = random()
        lanzamientos += 1
        if var_random < 0.5:
            caras += 1
        else:
            secas += 1
    return lanzamientos