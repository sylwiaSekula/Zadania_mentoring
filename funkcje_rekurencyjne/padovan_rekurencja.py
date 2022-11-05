def pad(n):
    if n < 0:
        raise ValueError('N nie może być liczbą ujemną')
    if n < 3:
        return 1
    else:
        return pad(n-2) + pad(n-3)


def main():
    n = 20
    print(pad(n))


if __name__ == '__main__':
    main()
