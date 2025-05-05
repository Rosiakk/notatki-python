import matplotlib.pyplot as plt
from wykresy import *

def draw_graph_slupkowy():
    x = ['A', 'B', 'C']
    y = [10, 15, 7]

    plt.bar(x, y)
    plt.title("Wykres słupkowy")
    plt.show()

def kilka_wykresow():
    x = [1, 2, 3, 4]
    y1 = [1, 4, 9, 16]
    y2 = [1, 2, 3, 4]

    plt.plot(x, y1, label="Kwadraty")
    plt.plot(x, y2, label="Liniowo")

    plt.legend()
    plt.title("Dwa wykresy")
    plt.show()
#    plt.savefig("wykres.png")   zapis do pliku


def draw_graph(data):
    hours = data['hourly']['time'][:24]
    temperatures = data['hourly']['temperature_2m'][:24]
    odczuwalna_temperatura = data['hourly']['apparent_temperature'][:24]
    opady = data['hourly']['precipitation'][:24]

    plt.figure(figsize=(12, 6))  # rozmiar okna wykresu w calach (szerokość x wysokość)
    plt.plot(
        hours, temperatures,
        marker='o',           # kropki na punktach
        linestyle='-',        # linia ciągła
        color='orange',       # kolor linii
        label='Temperatura (°C)'  # opis linii do legendy
    )
    plt.plot(hours, odczuwalna_temperatura, marker='o', linestyle='-', color = 'black', label = 'Temperatura odczuwalna')

    plt.bar(hours, opady, label='Opady [mm]', color='blue', alpha=0.5)


    plt.xticks(rotation=45, ha='right')  # obrót etykiet X o 45 stopni
    plt.xlabel("Godzina")
    plt.ylabel("Temperatura [°C]")
    plt.title("Temperatura w kolejnych godzinach")
    plt.grid(True)        # siatka na wykresie
    plt.legend()          # pokaż legendę
    plt.tight_layout()    # automatyczne dopasowanie elementów
    plt.show()


def draw_better_graph(data):
    hours = data['hourly']['time'][:24]
    temperatures = data['hourly']['temperature_2m'][:24]
    odczuwalna_temperatura = data['hourly']['apparent_temperature'][:24]
    opady = data['hourly']['precipitation'][:24]

    sunrise = datetime.fromisoformat(data['daily']['sunrise'][1])
    sunset = datetime.fromisoformat(data['daily']['sunset'][0])

    hours_dt = [datetime.fromisoformat(h) for h in hours]




    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(hours_dt, temperatures, color = 'yellow', marker = 'o', label = 'Temperatura')
    ax1.plot(hours_dt, odczuwalna_temperatura, color = 'black',marker = 'o', label = 'Odczuwalna temperatura')
    ax1.set_xlabel("Godzina")
    ax1.set_ylabel("Temperatura")
    ax1.axvspan(sunset,sunrise, facecolor = 'gray', alpha = 0.2, label = 'Noc') #zaznacza opszar od sunset do sunrise
    ax1.grid(True)
    ax1.tick_params(axis='x', rotation=45)

    ax2 = ax1.twinx()
    ax2.bar(hours_dt, opady, color = 'blue', label = 'Opady [mm]')
    ax2.set_ylabel("Opady [mm]")

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()

    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    plt.title("Dwa wykresy")
    plt.tight_layout()

    #plt.savefig('graph.png')

    plt.show()




if __name__ == "__main__":
    #draw_graph(data)
    draw_better_graph(data)

