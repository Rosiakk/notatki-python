from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QGridLayout, QMessageBox, QListWidget, \
    QListWidgetItem

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDoList")
        self.edit = QLineEdit(self)
        self.button = QPushButton("Dodaj zadanie")
        self.list = QListWidget(self)
        self.count = QLabel(self)
        self.deleted = QPushButton("Usun zadanie")

        self.button.clicked.connect(self.on_button_clicked)
        self.deleted.clicked.connect(self.delete_task)

        layout = QGridLayout(self)
        layout.addWidget(self.edit, 0, 1)
        layout.addWidget(self.button, 0, 0)
        layout.addWidget(self.list, 1, 0,1,2) # Dodaje do wiersza 1, kolumna 0, i rozciąga ją na 2 kolumny (kolumny 0 i 1)
        layout.addWidget(self.count, 2, 0,1,2 )# Dodaje etykietędo wiersza 2, kolumna 0, też na całą szerokość (2 kolumny)
        layout.addWidget(self.deleted, 3, 0,1,2)

    def on_button_clicked(self):
        self.list.addItem(self.edit.text())
        self.ilezadan()
        self.edit.clear()

    def ilezadan(self):
        count = str(self.list.count())
        self.count.setText("Liczba zadań: " + count)

    def delete_task(self):
        item = self.list.currentItem()
        if item:
            self.list.takeItem(self.list.row(item))
            self.ilezadan()