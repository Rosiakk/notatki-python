import numpy as np


def ex1():
    array2 = np.array([1,2,3,4],dtype=np.uint8)
    array = np.array([[1,2,3,4,5],[1,2,3,4,5]])
    print(array,array.shape,array.dtype)

def ex1_extended():
    # Tworzymy tablicę 2D: 2 wiersze, 5 kolumn
    array = np.array([[1, 2, 3, 4, 5],
                      [6, 7, 8, 9, 10]])

    print("Oryginalna tablica:")
    print(array)

    # 1. Typ danych
    print("\nTyp danych (dtype):", array.dtype)

    # 2. Kształt tablicy
    print("Kształt (shape):", array.shape)

    # 3. Zmiana typu danych
    array_float = array.astype(np.float32)
    print("\nPo konwersji na float32:")
    print(array_float)
    print("Nowy dtype:", array_float.dtype)

    # 4. Zmiana kształtu (reshape)
    reshaped = array.reshape((5, 2))  # 5 wierszy, 2 kolumny
    print("\nPo zmianie kształtu (reshape na 5x2):")
    print(reshaped)

    # 5. Dostęp do elementów
    print("\nElement w wierszu 1, kolumnie 2:", array[1, 2])  # 8
    print("Cały pierwszy wiersz:", array[0])
    print("Cała druga kolumna:", array[:, 1])

def zadanie1():
    a = np.arange(10,55,5)
    #b = np.array([[1,2,3],[4,5,6],[7,8,9]])
    b = np.arange(1, 10).reshape(3, 3)
    c = (a *10)/2
    filtered = b[b > 70]
    losowa = np.random.randint(1,100, size = (5,5))
    jednostkowa = np.eye(4)
    b_plus_10 = b + 10
    print("Dodane 10:\n", b_plus_10)

    b_times_2 = b * 2
    print("Pomnożone przez 2:\n", b_times_2)

    print(losowa)
    print(np.min(losowa))
    print(np.max(losowa))


    print(a)
    print(b)
    print(filtered)

    print(np.mean(b))

    row_sums = np.sum(b, axis=0)
    print(row_sums)
    print(np.sum(b))

    print(jednostkowa)

    b = np.array([[1, 2, 3], [4, 5, 6]])
    print("Oryginalna:\n", b)
    print("Transpozycja:\n", b.T)
    print("Kształt po transpozycji:", b.T.shape)
    # Wynik: (3, 2)

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    result = A.dot(B)
    print("Iloczyn macierzy:\n", result)
    # Wynik:
    # [[19 22]
    #  [43 50]]

    c = np.array([[1, 2, 3], [4, 5, 6]])
    add_vector = np.array([10, 20, 30])

    result = c + add_vector
    print("Po dodaniu wektora:\n", result)
    # Wynik:
    # [[11 22 33]
    #  [14 25 36]]


def main():

    a = np.array([1, 2, 3])
    b = np.array([[4, 5], [6, 7]])
    print(a)
    print(b)

    np.zeros((2,4))


if __name__ == '__main__':
    #main()
    #ex1()
    #ex1_extended()
    zadanie1()