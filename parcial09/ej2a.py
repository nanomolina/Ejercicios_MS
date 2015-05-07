from random import random

def rechazo():
    f = lambda x: 120 * (x**3) * ((1- x)**2)
    counter = 0
    while True:
        counter += 1
        Y = random()
        U = random()
        if U <= f(Y) * (5.0/3):
            result = Y
            break
    return result
