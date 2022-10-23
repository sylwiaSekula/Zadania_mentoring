import numpy as np


def density_normal_distr(sigma, my, x):
    return 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(((x-my)**2)/(2 * sigma**2)))


def integral_approximation(f, a, b):
    return (b-a)*np.mean(f)


def main():
    a = 4
    b = 16
    x = np.arange(a,b+0.0001,.00001)
    sigma = 3
    my = 10
    f = list(map(lambda x: density_normal_distr(sigma, my, x), x))
    print(integral_approximation(f, a, b))


if __name__ == "__main__":
    main()