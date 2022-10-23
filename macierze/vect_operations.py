import numpy as np


def sum_vects(vector, b):
    return vector + b


def add_scalar(vector, c):
    return vector + c


def mulitply_vect_p(vector, b):
    return vector * b


def mulitply_scalar(vector, c):
    return vector * c


def vect_multiplication(vector, b):
    return print(f'Wynikiem iloczynu wektorowego twojego wektora {vector} i wektora {b} jest wektor:' , [vector[1]*b[2]-vector[2]*b[1],vector[2]*b[0]-vector[0]*b[2],vector[0]*b[1]-vector[1]*b[0]])


def skalar_multiplication(vector, b):
    result = []
    for i, j in zip(vector, b):
        result.append(i*j)
    return print(f'Iloczyn skalarny twojego wektora {vector} i wektora {b} : mnożąc każdy element z twojego wektora przez każdy z drugiego wektora otrzymujemy:', result,'\n'
                 'wszystkie te liczby dodane do siebie dają iloczyn skalarny:', sum(result),'\n')


def main(vector, b, c):
    if len(vector) == len(b):
        print(f'Suma twojego wektora {vector} i wektora {b} daje wynik: {sum_vects(vector, b)}. Elementy wektorów są dodawane do siebie element po elemencie.\n')
        print(f'**Suma twojego wektora {vector} i skalaru, który jest liczbą {c} daje wynik: {add_scalar(vector, c)}. Do każdego elementu twojego wektora została dodana liczba {c}.\n')
        print(f'**Iloczyn twojego wektora {vector} i wektora {b} daje wynik: {mulitply_vect_p(vector, b)}. Elementy wektorów są mnożone element po elemencie.\n')
        print(f'Iloczyn twojego wektora {vector} i skalaru, który jest liczbą {c} daje wynik: {mulitply_scalar(vector, c)}. Każdy element twojego wektora został pomnożony przez liczbę {c}.\n')
        skalar_multiplication(vector, b)
        if len(vector) == 3 and len(b) == 3:
            vect_multiplication(vector, b)
        print('\n** ==>> oznacza, że takie działanie jest możliwe jedynie w programowaniu, z perspektywy matematycznej nie jest możliwe!!')
    else:
        raise ValueError('Vector i b muszą być tej samej długości')


if __name__ == '__main__':
    vector = np.array([1, 3, 5])
    b = np.array([2, 4, 6])
    c = 3
    main(vector, b, c)


