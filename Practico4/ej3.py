# -*- coding: utf-8 -*-
from random import random
import argparse

NUM_DADOS = range(1, 7)


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=100,
                       help='Cantidad de numeros aleatorios')
    return parser.parse_args()


def getCoupleSum():
    d1 = int(len(NUM_DADOS) * random() + 1)
    d2 = int(len(NUM_DADOS) * random() + 1)
    return d1 + d2


def ejA():
    results = range(2, 13)
    count = 0
    while len(results) > 0:
        sum_dados = getCoupleSum()
        count += 1
        if sum_dados in results:
            results.remove(sum_dados)
    return count


def ejB():
    args = parser()
    total = 0.0
    for i in range(args.n):
        total += ejA()
    expectation = total / args.n
    print "El valor medio en %s " \
        "iteraciones es %s" % (str(args.n), str(expectation))

if __name__ == "__main__":
    print "Numero de lanzamientos necesarios: ", ejA()
    ejB()

