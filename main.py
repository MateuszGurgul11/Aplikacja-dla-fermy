import datetime
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QDateEdit, QLineEdit

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.date_label = QLabel("Data wstawienia:", self)
        self.date_input = QDateEdit(self)
        self.date_input.setCalendarPopup(True)  # Umożliwia wybór daty z kalendarza
        
        self.qty_label = QLabel("Ilość sztuk:", self)
        self.qty_input = QLineEdit(self)

        self.result_label = QLabel("Wynik:", self)
        self.result_display = QLabel("", self)

        calculate_btn = QPushButton('Oblicz', self)
        calculate_btn.clicked.connect(self.calculate_and_display)

        quit_btn = QPushButton('Quit', self)
        quit_btn.clicked.connect(QApplication.instance().quit)

        layout = QVBoxLayout()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.qty_label)
        layout.addWidget(self.qty_input)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)
        layout.addWidget(calculate_btn)
        layout.addWidget(quit_btn)

        self.setLayout(layout)
        self.setWindowTitle("Prosty Program Okienkowy")
        self.setFixedSize(400, 600)

    def calculate_and_display(self):
        date = self.date_input.date().toPython()
        qty_str = self.qty_input.text()

        try:
            date_after_84 = date + datetime.timedelta(days=84)
            qty = int(qty_str)
            result = self.calculate_percentage(qty)
            self.result_display.setText(f"Data zdania: {date_after_84}\nIlość sztuk do zdania: {result}")
        except ValueError:
            self.result_display.setText("Nieprawidłowe dane wejściowe")

    def calculate_percentage(self, items):
        percentage = items * 0.025
        items -= percentage
        return round(items)

if __name__ == "__main__":
    app = QApplication([])
    app_window = AppWindow()
    app_window.show()
    app.exec()
