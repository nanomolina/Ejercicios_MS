import MonteCarlo
from math import e


def g(variables):
    assert(len(variables) == 2)

    x = variables[0]
    y = variables[1]
    return e ** ((x + y) ** 2)


def main():
    result = MonteCarlo.runMultipleVar(g, 2)
    print "resultado = ", result


if __name__ == "__main__":
    main()