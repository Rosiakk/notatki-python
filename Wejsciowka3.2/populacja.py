import matplotlib.pyplot as plt
import random

# 1. Stwórz dwa wykresy (fig, (ax1, ax2) = plt.subplots(2, 1, ...))
# 2. ax1 → wykres słupkowy populacji w jednym, wybranym roku (np. 2024)
# 3. ax2 → wykres liniowy populacji wybranego miasta w czasie
# 4. Kliknięcie słupka = aktualizacja ax2


lata = list(range(2015, 2025))
miasta = ["Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań"]

# Generowanie danych populacji
dane = {
    miasto: [random.randint(500000, 2000000) for _ in lata]
    for miasto in miasta
}

# Globalne referencje do potrzebnych elementów
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
słupki = []  # do przechowania referencji do słupków

def draw_graph():
    global słupki
    rok = 2024
    index = lata.index(rok)
    populacje = [dane[m][index] for m in miasta]

    # Wykres słupkowy
    bars = ax1.bar(miasta, populacje, color='skyblue')
    słupki = list(bars)  # zapamiętaj słupki!
    ax1.set_title(f"Populacja miast w {rok}")
    ax1.set_ylabel("Liczba mieszkańców")
    ax1.grid(True)

    # Domyślny wykres liniowy
    draw_line_plot("Warszawa")

def draw_line_plot(miasto):
    ax2.clear()
    ax2.plot(lata, dane[miasto], marker="o", color="blue", label=miasto)
    ax2.set_title(f"Populacja: {miasto}")
    ax2.set_xlabel("Rok")
    ax2.set_ylabel("Liczba mieszkańców")
    ax2.grid(True)
    ax2.legend()
    fig.canvas.draw_idle()

def onclick(event):
    if event.inaxes != ax1:
        return

    for rect, miasto in zip(słupki, miasta):
        contains, _ = rect.contains(event)
        if contains:
            draw_line_plot(miasto)
            break

# Główna logika
draw_graph()
fig.canvas.mpl_connect("button_press_event", onclick)
plt.tight_layout()
plt.show()


if __name__ == '__main__':
    draw_graph()
