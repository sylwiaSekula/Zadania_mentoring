import numpy as np


def sum_matrixs(matrix, matrix2):
    return matrix + matrix2


def sum_matrix_vect(matrix, vector):
    return matrix + vector


def adding_scalar(matrix, scalar):
    return matrix + scalar


def multiply_matrix(matrix, matrix2):
    return matrix * matrix2


def multiply_matrix_vect(matrix, vector):
    return matrix * vector


def multiply_scalar(matrix, scalar):
    return matrix * scalar


def math_multiply_matrixs(matrix, matrix2):
    return matrix @ matrix2


def main(matrix, matrix2, vector, scalar):
        if matrix.shape == matrix2.shape:
            print(f'1.Suma twojej macierzy \n{matrix}\ni macierzy\n {matrix2}\n daje wynik: \n{sum_matrixs(matrix, matrix2)}. Elementy macierzy są dodawane do siebie element po elemencie.\n')
            print(f'2.Suma twojej macierzy \n{matrix}\ni wektora {vector} daje wynik:\n{sum_matrix_vect(matrix, vector)}. Do każdego wiersza twojej macierzy został dodany wektor{vector}.\n')
            print(f'2.Suma twojej macierzy \n{matrix}\ni skalaru, który jest liczbą {scalar} daje wynik: \n{adding_scalar(matrix, scalar)}. Do każdego elementu twojej macierzy została dodana liczba {scalar}.\n')
            print(f'4.Iloczyn twojej macierzy \n{matrix}\ni macierzy\n {matrix2}\n daje wynik: \n{multiply_matrix(matrix, matrix2)}. Elementy macierzy są mnożone element po elemencie.\n')
            print(f'5.Iloczyn twojej macierzy \n{matrix}\ni wektora {vector} daje wynik:\n{multiply_matrix_vect(matrix, vector)}. Każdy wiersz twojej macierzy został pomnożony wektor{vector}.\n')
            print(f'6.Iloczyn twojej macierzy \n{matrix}\ni skalaru, który jest liczbą {scalar} daje wynik: \n{multiply_scalar(matrix, scalar)}. Każdy element twojej macierzy został pomnożony przez liczbę {scalar}.\n')
            print(f'7.Matematyczny iloczyn twojej macierzy \n{matrix}\ni macierzy\n{matrix} daje wynik:\n',math_multiply_matrixs(matrix, matrix2))
            print('Każdy element z wiersza twojej macierzy został pomnożony przez element z kolumny drugiej macierzy')


if __name__ == '__main__':
    matrix = np.array([[2, 3, 4], [5, 6, 7], [1, 2, 3]])
    matrix2 = np.array([[2, 1, 1], [1, 2, 7], [1, 2, 1]])
    vector = np.array([2, 3, 5])
    scalar = 5
    main(matrix, matrix2, vector, scalar)