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

    result = random()
    var1 = random()
    count = 1
    for i in range(args.n - 1):
        result += var1
        count += 1
        if result > 1:
            break
        else:
            var1 = random()

    print "en " + str(args.n) + " vueltas la cantidad de numeros " \
        "que deben sumarse para exceder a 1 es: " + str(count)

if __name__ == "__main__":
    main()
