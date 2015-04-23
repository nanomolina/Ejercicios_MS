# -*- coding: utf-8 -*-
from random import random
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
        while(True):
            var1 = random()
            result += var1
            count += 1
            if result > 1:
                break
        prom += count
    prom /= args.n

    print "en " + str(args.n) + " vueltas E[N] = " + str(prom)


if __name__ == "__main__":
    main()
