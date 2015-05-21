from random import random
from math import exp, sqrt


def mean(sample):
    return sum(sample) / float(len(sample))


def variance(sample, v_mean):
    suma = 0.0
    for elem in sample:
        suma += (elem - v_mean) ** 2
    return suma / float(len(sample) - 1)


def g(x):
    return exp(x**2)


def main(fun):
    result = 0.0
    sample = [fun(random()) for _ in range(100)]
    while True:
        v_mean = mean(sample)
        ds_std = sqrt(variance(sample, v_mean))
        if ds_std / sqrt(len(sample)) < 0.01:
            break
        else:
            sample.append(fun(random()))        
    return len(sample)


if __name__ == "__main__":
    print "LEN:", main(g)
