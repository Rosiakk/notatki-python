import math
from datetime import datetime, timedelta
import geopandas as gpd
import matplotlib.pyplot as plt
import requests
from polska import cities


miasta = [
    ("Warszawa", 52.23, 21.01, 1800000),
    ("Kraków", 50.06, 19.94, 780000),
    ("Łódź", 51.76, 19.45, 670000),
    ("Wrocław", 51.10, 17.03, 640000),
    ("Poznań", 52.41, 16.93, 540000)
]


class PolandMap:
    def __init__(self, shapefile_url=None):
        default_url = 'https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip'
        self.shapefile_url = shapefile_url or default_url
        self._world = gpd.read_file(self.shapefile_url)
        self.poland = self._world[self._world['ADMIN'] == 'Poland']
        self.active_index = 0

    def draw(self):
        fig, (map_ax, ax2) = plt.subplots(2,1,figsize=(8,10))
        self.fig = fig
        self.map_ax = map_ax
        self.ax2 = ax2

        self.poland.plot(ax=map_ax, color='lightgrey', edgecolor='black')
        self.draw_city(map_ax, fig)
        self.draw_slupek(ax2)

        self.fig.canvas.mpl_connect("button_press_event", self.onclick)

        plt.tight_layout()

    def draw_city(self, ax, fig):
        x = [miasto[2] for miasto in miasta]
        y= [miasto[1] for miasto in miasta]

        c = [miasto[3] for miasto in miasta]
        sizes = [v / 50000 for _, _, _, v in miasta]  # im więcej ludzi, tym większe
        plot = ax.scatter(x, y, c=c, s=sizes, cmap="Reds")

        fig.colorbar(plot, ax=ax, label='Liczba ludnosci', cmap = 'Reds')

        for name, lat, lon, value in miasta:
            ax.text(lon + 0.2, lat + 0.2, name)

    def draw_slupek(self, ax2):
        city_index = self.active_index
        name, lat, lon, value = miasta[city_index]

        ax2.clear()
        ax2.bar([name], [value], color='green')
        ax2.set_title(f"Liczba ludności w: {name}")
        ax2.set_ylabel("Liczba mieszkańców")

    def onclick(self, event):
        if event.inaxes != self.map_ax:
            return

        click_x, click_y = event.xdata, event.ydata
        closest_index = None
        min_dist = float('inf')

        for i, (_, lat, lon, _) in enumerate(miasta):
            dist = math.hypot(lon - click_x, lat - click_y)
            if dist < min_dist and dist < 0.5:
                closest_index = i
                min_dist = dist

        if closest_index is not None:
            self.active_index = closest_index
            self.draw_slupek(self.ax2)
            self.fig.canvas.draw_idle()


if __name__ == '__main__':
    poland = PolandMap()
    poland.draw()
    plt.show()