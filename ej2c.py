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
    wins = 0

    for i in range(args.n):
        var = random()
        if var < 1.0 / 2.0:
            var1 = random()
            var2 = random()
            x = var1 + var2
        else:
            var1 = random()
            var2 = random()
            var3 = random()
            x = var1 + var2 + var3
        if x >= 1:
            wins += 1

    print "en " + str(args.n) + " vueltas se ganaron " + str(wins) + " veces!!"

if __name__ == "__main__":
    main()