import numpy as np


def density_normal_distr(sigma, my, x):
    if isinstance(x, (int, float)):
        return 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(((x-my)**2)/(2 * sigma**2)))
    result = []
    for element in x:
        result.append(1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(((element-my)**2)/(2 * sigma**2))))
    return result


def integral_approximation(f, a, b):
    return (b-a)*np.mean(f)


def main():
    sigma = 1
    my = 0
    a = -2
    b = 2
    x = np.arange(a, b + 0.0001, .00001)
    f = density_normal_distr(sigma, my, x)
    print(integral_approximation(f, a, b))


if __name__ == '__main__':
    main()
