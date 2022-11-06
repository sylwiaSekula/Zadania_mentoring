def silnia_for(n):
    if n <= 0:
        raise ValueError('N musi być większe od 0')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    n = 777
    print(silnia_for(n))


if __name__ == '__main__':
    main()
