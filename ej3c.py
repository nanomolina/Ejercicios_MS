import MonteCarlo
from math import e


def h(y):
    a = (1 / y) - 1
    b = -(a ** 2)
    c = y ** 2
    d = e ** b
    return d / c


def main():
    result = MonteCarlo.run(h)
    result *= 2
    print "resultado = ", result


if __name__ == "__main__":
    main()