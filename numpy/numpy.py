import numpy as np

# === 1. Tworzenie tablic ===
np.array([1, 2, 3])                     # z listy
np.zeros((3, 3))                        # same zera
np.ones((2, 4))                         # same jedynki
np.eye(3)                               # macierz jednostkowa
np.full((2, 3), 7)                      # tablica wypelniona 7
np.arange(0, 10, 2)                     # [0 2 4 6 8]
np.linspace(0, 1, 5)                    # [0. 0.25 0.5 0.75 1.]

# === 2. Kształt i rozmiar ===
a.shape                                 # kształt (np. (3, 3))
a.ndim                                  # liczba wymiarów
a.size                                  # liczba elementów
a.reshape(1, -1)                        # zmiana kształtu
a.T                                     # transpozycja

# === 3. Indeksowanie i cięcie ===
a[1]                                    # 1 element
a[1:4]                                  # wycinek 1D
a[:, 0]                                 # 1. kolumna
a[0, :]                                 # 1. wiersz
a[::2]                                  # co drugi element

# === 4. Operacje matematyczne ===
a + b                                   # dodawanie
a * b                                   # mnożenie element po elemencie
a ** 2                                  # potęgowanie
np.sqrt(a)                              # pierwiastek
np.dot(a, b)                            # iloczyn macierzy
np.sum(a, axis=0)                       # suma po kolumnach

# === 5. Statystyka ===
np.mean(a)                              # średnia
np.std(a)                               # odchylenie standardowe
np.min(a), np.max(a)                    # min i max
np.median(a)                            # mediana
np.percentile(a, 90)                    # 90-ty percentyl

# === 6. Filtrowanie / maski ===
a[a > 5]                                # wybierz tylko > 5
mask = a % 2 == 0
a[mask]                                 # liczby parzyste

# === 7. Losowe dane ===
np.random.randint(0, 10, (2, 3))        # losowe liczby całkowite
np.random.rand(3, 3)                    # losowe [0, 1)
np.random.normal(0, 1, (100,))          # rozkład normalny
np.random.seed(42)                      # ustalenie ziarna

# === 8. Funkcje logiczne ===
np.any(a > 5)                           # czy jakikolwiek > 5
np.all(a > 0)                           # czy wszystkie > 0
np.where(a > 10, 1, 0)                  # warunkowe podstawienie

# === 9. Zaokrąglanie i typy danych ===
np.round(a, 2)                          # zaokrąglenie do 2 miejsc
a.astype(np.uint8)                     # zmiana typu danych

# === 10. Operacje na wielu tablicach ===
np.concatenate([a, b], axis=0)          # łączenie wierszy
np.stack([a, b], axis=0)                # dodanie nowego wymiaru

# === 11. Specjalne funkcje ===
np.clip(a, 0, 255)                      # przycinanie wartości
np.meshgrid(x, y)                       # siatka współrzędnych (do wizualizacji)
