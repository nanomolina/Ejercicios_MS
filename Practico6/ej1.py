from random import normalvariate
from math import sqrt


def mean(sample):
    return sum(sample) / float(len(sample))


def variance(sample, v_mean):
    suma = 0.0
    for elem in sample:
        suma += (elem - v_mean) ** 2
    return suma / float(len(sample) - 1)


def main():
    sample = [normalvariate(0, 1) for _ in range(30)]
    while True:
        v_mean = mean(sample)
        ds_std = sqrt(variance(sample, v_mean))
        if ds_std / sqrt(len(sample)) < 0.1:
            break
        else:
            sample.append(normalvariate(0, 1))
    return len(sample)


if __name__ == "__main__":
    print "LEN", main()

