import numpy as np


def density_exp_distr(lamb, x):
    if x < 0:
        return 0
    return lamb * (np.exp(-lamb * x))


def integral_approximation(f, a, b):
    return (b - a) * np.mean(f)


def main():
    lamb = 1.5
    a = 0
    b = 3
    x = np.arange(a, b + 0.0001, .0001)
    f = list(map(lambda x: density_exp_distr(lamb, x), x))
    print(integral_approximation(f, a, b))


if __name__ == "__main__":
    main()