import geopandas as gpd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import requests

# Lista miast z ich współrzędnymi geograficznymi (nazwa, szerokość, długość)
cities = [
    ("Warszawa", 52.2297, 21.0122),
    ("Kraków", 50.0647, 19.9450),
    ("Łódź", 51.7592, 19.4560),
    ("Wrocław", 51.1079, 17.0385),
    ("Poznań", 52.4064, 16.9252),
    ("Gdańsk", 54.3520, 18.6466),
    ("Szczecin", 53.4285, 14.5528),
    ("Bydgoszcz", 53.1235, 18.0084),
    ("Lublin", 51.2465, 22.5684),
    ("Katowice", 50.2649, 19.0238),
    ("Białystok", 53.1325, 23.1688),
    ("Rzeszów", 50.0413, 21.9990),
    ("Olsztyn", 53.7784, 20.4801),
    ("Kielce", 50.8661, 20.6286),
    ("Opole", 50.6751, 17.9213),
    ("Zielona Góra", 51.9355, 15.5062)
]

class PolandMap:
    def __init__(self, shapefile_url=None):
        # Adres domyślnego pliku shape (granice krajów)
        default_url = 'https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip'
        self.shapefile_url = shapefile_url or default_url

        # Wczytanie danych geograficznych (wszystkie kraje)
        self._world = gpd.read_file(self.shapefile_url)

        # Filtrujemy tylko dane dla Polski
        self.poland = self._world[self._world['ADMIN'] == 'Poland']

        # Domyślnie pokazujemy dane dla pierwszego miasta (Warszawa)
        self.active_index = 0

        # Pobranie danych pogodowych dla wszystkich miast
        self.data = self.get_data()

    def get_data(self):
        # Ustaw daty (dziś i jutro)
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=1)

        results = []

        # Dla każdego miasta wykonujemy osobne zapytanie do API
        for name, lat, lon in cities:
            url = (
                f"https://api.open-meteo.com/v1/forecast?"
                f"latitude={lat}&longitude={lon}"
                f"&hourly=temperature_2m"
                f"&start_date={start_date}&end_date={end_date}"
                f"&timezone=Europe/Warsaw"
            )

            response = requests.get(url)
            if response.status_code == 200:
                try:
                    results.append(response.json())
                except Exception as e:
                    print(f"Błąd JSON dla {name}: {e}")
                    results.append({})
            else:
                print(f"Błąd pobierania danych dla {name}: {response.status_code}")
                results.append({})
        return results

    def draw(self):
        # Utwórz dwa podwykresy: mapa i wykres temperatury
        fig, (ax_map, ax_temp) = plt.subplots(2, 1, figsize=(10, 12), gridspec_kw={'height_ratios': [2, 1]})
        self.fig = fig
        self.ax_map = ax_map
        self.ax_temp = ax_temp

        # Narysuj Polskę na mapie
        self.poland.plot(ax=ax_map, color='lightgrey', edgecolor='black')

        # Narysuj miasta i temperatury na mapie
        self.draw_cities(ax_map, self.data, fig)

        # Narysuj wykres temperatury dla aktywnego miasta
        self.draw_city_label()

        # Tytuł całej figury
        fig.suptitle("Mapa Polski z zaznaczonymi miastami i wykresem temperatury", fontsize=14)

        # Obsługa kliknięcia myszą na mapie
        fig.canvas.mpl_connect("button_press_event", self.onclick)

    def draw_cities(self, ax, data, fig):
        # Pobierz współrzędne i temperatury (godzina 0) do pokolorowania punktów
        x = [city[2] for city in cities]
        y = [city[1] for city in cities]
        c = [entry["hourly"]["temperature_2m"][0] for entry in data]

        # Rysuj miasta jako kolorowe punkty
        plot = ax.scatter(x, y, c=c, cmap="Spectral_r")
        fig.colorbar(plot, ax=ax, label="Temperatura (°C)")

        # Dodaj etykiety do każdego miasta (nazwa i temperatura)
        for city, entry in zip(cities, data):
            name, lat, lon = city
            temp = entry["hourly"]["temperature_2m"][0]
            ax.text(lon + 0.1, lat + 0.1, name, fontsize=8)
            ax.text(lon + 0.1, lat - 0.2, f"{temp:.1f}°C", fontsize=8, color='blue')

    def draw_city_label(self):
        # Czyść dolny wykres (temperatury)
        self.ax_temp.clear()
        city_index = self.active_index

        # Wybierz dane pogodowe dla aktywnego miasta
        city_data = self.data[city_index]["hourly"]
        hours = city_data["time"][:24]
        temperatures = city_data["temperature_2m"][:24]
        times = [datetime.fromisoformat(t) for t in hours]

        # Narysuj wykres temperatury godzinowej
        self.ax_temp.plot(times, temperatures, label='Temperatura', color='blue', marker='o')
        self.ax_temp.set_title(f"Wykres temperatury: {cities[city_index][0]}")
        self.ax_temp.set_xlabel("Godzina")
        self.ax_temp.set_ylabel("°C")
        self.ax_temp.grid(True)
        self.ax_temp.tick_params(axis='x', labelrotation=45)

        # Odśwież tylko wykres (bez tworzenia nowego okna)
        self.fig.canvas.draw_idle()

    def onclick(self, event):
        # Jeżeli kliknięto poza mapą, ignoruj
        if event.inaxes != self.ax_map:
            return

        click_x, click_y = event.xdata, event.ydata
        closest_index = None
        min_dist = float('inf')

        # Sprawdź, które miasto jest najbliżej kliknięcia
        for i, (_, lat, lon) in enumerate(cities):
            dist = ((lon - click_x) ** 2 + (lat - click_y) ** 2) ** 0.5
            if dist < min_dist and dist < 0.5:  # tolerancja kliknięcia
                closest_index = i
                min_dist = dist

        # Jeśli znaleziono miasto, zaktualizuj aktywny indeks i wykres
        if closest_index is not None:
            self.active_index = closest_index
            self.draw_city_label()

# Start programu
if __name__ == '__main__':
    poland = PolandMap()
    poland.draw()
    plt.show()
