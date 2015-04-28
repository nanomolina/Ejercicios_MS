# -*- coding: utf-8 -*-
from random import random
from math import sqrt
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
    for _ in range(args.n):
        total += successPackOfCards()
    average = total / int(args.n)
    return average

def Variance():
    args = parser()
    total = 0.0
    average = expectation()
    for _ in range(args.n):
        total = (successPackOfCards() - average)**2
    variance = total / (args.n - 1)
    return variance


if __name__ == "__main__":
    average = expectation()
    print "La esperanza en %s iteraciones es: %s" % (100, str(average))
    variance = Variance()
    print "La varianza en %s iteraciones es: %s" % (100, str(variance))
    print "La desv std en %s iteraciones es: %s" % (100, str(sqrt(variance)))
