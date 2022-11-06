def silnia_reku(n):
    if n in [0, 1]:
        return 1
    elif n < 0:
        raise ValueError('N musi być większe od 0')
    return n * (silnia_reku(n - 1))


def main():
    n = 9
    print(silnia_reku(n))


if __name__ == '__main__':
    main()



