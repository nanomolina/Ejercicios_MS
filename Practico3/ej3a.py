import MonteCarlo


def g(x):
    return x * (1 + x ** 2) ** (-2)


def main():
    result = MonteCarlo.run(g)
    print "resultado = ", result


if __name__ == "__main__":
    main()