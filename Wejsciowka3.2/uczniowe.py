from matplotlib import pyplot as plt

uczniowie = ["Anna", "Bartek", "Celina", "Dawid", "Ela"]

wyniki = {
    "Anna": {"matematyka": 85, "fizyka": 78, "polski": 92},
    "Bartek": {"matematyka": 65, "fizyka": 58, "polski": 75},
    "Celina": {"matematyka": 90, "fizyka": 95, "polski": 88},
    "Dawid": {"matematyka": 40, "fizyka": 60, "polski": 55},
    "Ela": {"matematyka": 70, "fizyka": 85, "polski": 80}
}


def draw_graph():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

    przedmiot = "matematyka"

    x = uczniowie
    y = [wyniki[uczen][przedmiot] for uczen in uczniowie]

    ax1.bar(x, y, color='skyblue')
    ax1.set_title(f"Wyniki z {przedmiot}")
    ax1.set_ylabel("Punkty")
    ax1.grid(True)

    osoba = "Celina"
    przedmioty = list(wyniki[osoba].keys())
    punkty = list(wyniki[osoba].values())

    ax2.plot(przedmioty, punkty, marker="o", color="green")
    ax2.set_title(f"Wyniki ucznia: {osoba}")
    ax2.set_ylabel("Punkty")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    draw_graph()



# # Globalne zmienne
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
# słupki = []
# przedmiot = "matematyka"
#
# def draw_graph():
#     global słupki
#     ax1.clear()
#     ax2.clear()
#
#     # Słupki dla danego przedmiotu
#     y = [wyniki[uczen][przedmiot] for uczen in uczniowie]
#     bars = ax1.bar(uczniowie, y, color='skyblue')
#     słupki = list(bars)
#
#     ax1.set_title(f"Wyniki z {przedmiot}")
#     ax1.set_ylabel("Punkty")
#     ax1.grid(True)
#
#     # Domyślnie pokazujemy pierwszego ucznia
#     draw_line_chart("Anna")
#
#     fig.canvas.draw_idle()
#
# def draw_line_chart(imie):
#     ax2.clear()
#     przedmioty = list(wyniki[imie].keys())
#     punkty = list(wyniki[imie].values())
#
#     ax2.plot(przedmioty, punkty, marker="o", color="green")
#     ax2.set_title(f"Wyniki ucznia: {imie}")
#     ax2.set_ylabel("Punkty")
#     ax2.grid(True)
#
# def onclick(event):
#     if event.inaxes != ax1:
#         return
#
#     for bar, uczen in zip(słupki, uczniowie):
#         contains, _ = bar.contains(event)
#         if contains:
#             draw_line_chart(uczen)
#             break
#
# draw_graph()
# fig.canvas.mpl_connect("button_press_event", onclick)
# plt.tight_layout()
# plt.show()
