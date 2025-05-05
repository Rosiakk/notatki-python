# notatki-python

https://github.com/kdmitruk/python_lab_2025

t.figure(figsize=(...)) - Tworzy nowy obiekt wykresu o określonym rozmiarze (w calach).

plt.subplots(figsize=(...))  - Tworzy nowy obiekt figure i oś wykresu (ax1).

ax1.twinx() - Dodaje drugą oś Y.

ax1.plot(x, y, ...) - Rysuje wykres liniowy na osi ax1.

ax2.bar(x, y, ...) - Rysuje wykres słupkowy na osi ax2.

ax1.axvspan(start, end, ...) - Zaznacza tło wykresu między dwiema godzinami.

ax1.set_xlabel("...") - Ustawia etykietę osi X.

ax1.set_ylabel("...") - Ustawia etykietę osi Y.

ax2.set_ylabel("...") - Ustawia etykietę osi Y dla drugiej osi.

ax1.set_title("...") - Ustawia tytuł wykresu.

ax1.tick_params(...) - Ustawia wygląd osi (np. obrót etykiet X).

plt.xticks(rotation=..., ha='right') - Obraca etykiety na osi X.

ax1.legend() - Wyświetla legendę.

ax1.get_legend_handles_labels() - Pobiera dane do połączonej legendy.

ax1.legend(l1 + l2, lbl1 + lbl2) - Łączy legendy z dwóch osi.

plt.tight_layout() - Dopasowuje marginesy wykresu.

plt.grid(True) - Włącza siatkę tła wykresu.

plt.show() - Pokazuje wykres.

ax1.xaxis.set_major_formatter(...) - Formatowanie godzin na osi X (np. %H:%M).
