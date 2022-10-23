import numpy as np


def density_exp_distr(lamb, x):
    if isinstance(x, (int, float)):
        if x < 0:
            return 0
        return lamb * (np.exp(-lamb *x))
    result = []
    for element in x:
        if element < 0 or element > 100000000:
            result.append(0)
        else:
            result.append(lamb * (np.exp(-lamb * element)))
    return result


def integral_approximation(f, a, b):
    return (b-a)*np.mean(f)


def main():
    print(integral_approximation(f, a, b))


if __name__ == '__main__':
    lamb = 1.5
    a = -5
    b = -1
    x =  np.arange(a, b+0.0001,.00001)
    f = density_exp_distr(lamb, x)
    main()
