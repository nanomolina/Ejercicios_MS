# -*- coding: utf-8 -*-
from random import random


def genVar():
    var_random = random()
    i = 1
    p = (1.0 / 4) + (1.0 / 6)
    F = p
    while var_random >= F:
        p =