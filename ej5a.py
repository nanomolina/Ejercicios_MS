# -*- coding: utf-8 -*-
from random import random
from math import e
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=100,
                       help='Cantidad de numeros aleatorios')
    return parser.parse_args()


def main():
    args = parser()

    prom = 0.0
    for i in range(args.n):
        result = random()
        count = 1
        while True:
            if result >= e ** -3:
                var = random()
                result *= var
                count += 1
            else:
                if count > 1:
                    count -= 1
                break
        prom += count
    prom /= args.n

    print "en " + str(args.n) + " vueltas E[N] = " + str(prom)


if __name__ == "__main__":
    main()