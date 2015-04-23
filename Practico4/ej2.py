# -*- coding: utf-8 -*-
from random import random
from math import e
import argparse

N = 10000


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=100,
                       help='Cantidad de numeros aleatorios')
    return parser.parse_args()


def funExp(k):
    return e ** (k / float(N))


def ejA():
    total = 0.0
    for i in range(N):
        total += funExp(i + 1)
    print "La cantidad deseada es: ", total


def ejB():
    args = parser()
    total = 0.0
    for _ in range(args.n):
        var_random = random()
        var = N * var_random + 1
        total += funExp(var)
    result = (total * N) / args.n
    print "Sorteando %s " \
        "num. aleat. es: %s" % (str(args.n), str(result))


if __name__ == "__main__":
    ejA()
    ejB()
