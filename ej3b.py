import MonteCarlo


def h(y):
    a = 1 - y
    b = y - 1
    c = y ** 2 - y + 1
    d = 1 / y
    return a / (4 * b * c + d)


def main():
    result = MonteCarlo.run(h)
    print "resultado = ", result


if __name__ == "__main__":
    main()