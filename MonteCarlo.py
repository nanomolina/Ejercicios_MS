import random
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=10000,
                       help='Cantidad de numeros aleatorios')
    return parser.parse_args()


def run(fun):
    args = parser()
    result = 0.0
    for i in range(args.n):
        var = random.random()
        result += fun(var)
    result = result / args.n
    return result


def runMultipleVar(fun, mount_vars):
    """
    fun debe recibir un arreglo de variables
    """
    args = parser()
    result = 0.0
    variables = []
    for i in range(args.n):
        for j in range(mount_vars):
            var = random.random()
            variables.append(var)
        result += fun(variables)
        variables = []
    result = result / args.n
    return result