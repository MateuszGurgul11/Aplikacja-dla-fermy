import datetime
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        quit_btn = QPushButton('Quit', self)
        quit_btn.move(320, 570)

        self.setFixedSize(400, 600)
        self.setWindowTitle("Test Window")

        self.show()

def calculate_procentage(items):
    procentage = items * 0.025
    items -= procentage
    return items

def get_date():
    while True:
        date_input = input("Wprowadz date wstawienia oddzielona '-' [rrrr, mm, dd]: ")
        try:
            year, month, day = map(int, date_input.split('-'))
            date = datetime.date(year, month, day)

            date_after_84 = date + datetime.timedelta(days = 84)
            print(f"Data wstawienia: {date}")

            return date_after_84

        except ValueError:
            print("Wprowadzona data nie jest poprawna! Sprobuj ponownie")

def get_items_count():
    while True:
        items = input("Podaj ilosc sztuk do wstawienia:  ")
        try: 
            items = int(items)
            result = calculate_procentage(items)
            print(f"Ilosc sztuk do wstawienia: {items}")
            return result
        except ValueError:
            print("Ilosc sztuk jest bledna! Sprobuj ponownie!")

def display_results(result, date_after_84):
    print(f"Data zdania: {date_after_84}\nIlosc sztuk do zdania: {result}")

def main():
    date_after_84 = get_date()
    result = get_items_count()
    print('------------------------------')
    display_results(result, date_after_84)

if __name__ == "__main__":
    #main()

    app = QApplication([])
    app_window = AppWindow()

    app.exec()