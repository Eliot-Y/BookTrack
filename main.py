from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys

from ui_main import Ui_MainWindow
import connection


class Booktrack(QMainWindow):
    def __init__(self):  # установка главного окна в соответствии со сделанным интерфейсом
        super(Booktrack, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db_object = connection.Connectdb()  # создание объекта БД

        # подключение методов к кнопкам
        self.ui.add_pushButton.clicked.connect(self.add_btn)
        self.ui.edit_pushButton.clicked.connect(self.del_btn)
        self.ui.del_pushButton.clicked.connect(self.edit_btn)
        self.ui.filter_pushButton.clicked.connect(self.filter_btn)
        self.ui.analytics_pushButton.clicked.connect(self.analytics_btn)

        # self.ui.tableView.

    def update_price_and_amount(self):  # обновление полей общего числа книг и общей цены книг
        self.ui.total_price_label.setText(self.db_object.get_sum_price())  # для цены
        self.ui.amount_label.setText(self.db_object.get_sum_amount())  # для количества

    def add_btn(self):
        self.db_object.add_transaction()
        # self.update_price_and_amount()
        print('add_btn')

    def del_btn(self):
        print('del_btn в разработке')

    def edit_btn(self):
        print('edit_btn в разработке')

    def filter_btn(self):
        print('filter_btn в разработке')

    def analytics_btn(self):
        print('analytics_btn в разработке')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # передача аргументов системы
    window = Booktrack()  # объект главного окна
    window.show()

    sys.exit(app.exec())
