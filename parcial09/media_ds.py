from math import sqrt

def meanAndVariance(fun, loops):
    muestra = []
    for _ in range(loops):
        muestra.append(fun())
    mean = sum(muestra)/float(loops)
    variance = 0
    for elem in muestra:
        variance = (elem - mean) ** 2
    variance /= float(loops - 1)
    return mean, variance, sqrt(variance)
