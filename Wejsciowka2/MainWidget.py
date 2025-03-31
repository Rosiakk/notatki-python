from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QGridLayout, QMessageBox, QListWidget, \
    QListWidgetItem
import requests


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stolica")
        self.label = QLabel(self)
        self.button = QPushButton("Szukaj")
        self.edit = QLineEdit(self)
        self.capital = QListWidget(self)

        self.button.clicked.connect(self.on_button_clicked)
        self.capital.itemClicked.connect(self.on_item_clicked)

        layout = QGridLayout(self)
        layout.addWidget(self.button, 0, 0)
        layout.addWidget(self.edit, 0, 1)
        layout.addWidget(self.capital, 1, 0, 1, 2)  # zajmuje całą szerokość (2 kolumny)
        layout.addWidget(self.label, 2, 0, 1, 2)  # etykieta też na całą szerokość

    def on_button_clicked(self):
        text = self.edit.text()
        response = requests.get(f"https://restcountries.com/v3.1/name/{text}")
        json_data = response.json()

        if not json_data:
            QMessageBox.information(self, "Błąd", "Nie znaleziono kraju.")
            return
        self.capital.clear()
        for country in json_data:
            name = country["name"]["common"]
            capital = country.get("capital", ["Brak stolicy"])[0]
            population = country.get("population", "Brak danych")

            item = QListWidgetItem(name)
            item.setData(Qt.UserRole, (capital, population))
            self.capital.addItem(item)


    def on_item_clicked(self, item):
        capital, population = item.data(Qt.UserRole)
        self.label.setText(f"Stolica: {capital}, Populacja: {population}")


