# -*- coding: utf-8 -*-
from random import random
import argparse

NUMBER_OF_CARDS = 100


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=100,
                       help='Cantidad de numeros aleatorios')
    return parser.parse_args()


def swap(array, i, j):
    var_temp = array[i]
    array[i] = array[j]
    array[j] = var_temp
    return array


def randomPermutation(array):
    k = len(array) - 1
    while k > 1:
        var_random = random()
        i = int(k * var_random)
        array = swap(array, k, i)
        k -= 1
    return array


def successPackOfCards():
    range_cards = range(1, NUMBER_OF_CARDS + 1)
    pack_of_cards = randomPermutation(range_cards)
    counter = 0
    for i in range(NUMBER_OF_CARDS):
        if i == pack_of_cards[i]:
            counter += 1
    return counter


def expectation():
    args = parser()
    total = 0.0
    for _ in range(int(args.n)):
        total += successPackOfCards()
    average = total / int(args.n)
    print "La esperanza en %s iteraciones es: %s" % (str(args.n), str(average))


if __name__ == "__main__":
    expectation()
