import numpy as np


def density_uniform_distr(a, b, x):
    if x < a or x > b:
        return 0
    return 1/(b-a)


def integral_approximation(f, a, b):
    return (b-a)*np.mean(f)


def main():
    a = 2
    b = 5
    c = 0
    d = 3
    x = np.arange(c,d+0.0001,.00001)
    f = list(map(lambda x: density_uniform_distr(a, b, x), x))
    print(integral_approximation(f, c, d))


if __name__ == '__main__':
    main()
