import numpy as np


def density_uniform_distr(x, a, b):
    if isinstance(x, (int, float)):
        if x < a or x > b:
            return 0
        return 1/(b-a)
    result = []
    for element in x:
        if element < a or element > b:
            result.append(0)
        else:
            result.append(1/(b-a))
    return result


def integral_approximation(f, a, b):
    return (b-a)*np.mean(f)


def main():
    a = 2
    b = 5
    c = 0
    d = 3
    x = np.arange(c, d + 0.0001, .00001)
    f = density_uniform_distr(x, a, b)
    print(integral_approximation(f, c, d))


if __name__ == '__main__':
    main()
