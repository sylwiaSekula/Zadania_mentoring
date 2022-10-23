def padov(n):
    if n < 0:
        raise ValueError('N nie może być liczbą ujemną')
    if n in (0, 1, 2):
        return 1
    padovan = [1, 1, 1]
    for n in range(3,  n+1):
        padovan.append(padovan[-2]+padovan[-3])
    return padovan[-1]


def main():
    print(padov(n))


if __name__ == '__main__':
    n = 200
    main()