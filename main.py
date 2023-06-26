from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from PyQt6.QtSql import QSqlTableModel
from ui_main import Ui_MainWindow
from connection import DataB
from ui_add_ed_window import Ui_Dialog


class Booktrack(QMainWindow):
    def __init__(self):  # установка главного окна в соответствии со сделанным интерфейсом
        super(Booktrack, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db_object = DataB()  # создание объекта БД
        self.db_object.create_connection()
        self.view_data()

        # подключение методов к кнопкам
        self.ui.add_pushButton.clicked.connect(self.open_new_window_ad_ed)
        self.ui.edit_pushButton.clicked.connect(self.open_new_window_ad_ed)
        self.ui.del_pushButton.clicked.connect(self.del_current_transaction)
        self.ui.filter_pushButton.clicked.connect(self.filter_lines)
        self.ui.analytics_pushButton.clicked.connect(self.analytics_data_base)

    def view_data(self):  # отображение данных из БД
        self.model = QSqlTableModel(self)
        self.model.setTable('books')  # соединение с таблицей
        self.model.select()  # выбрать данные
        self.ui.tableView.setModel(self.model)  # отображение таблицы

    def open_new_window_ad_ed(self):  # открывает окно ввода и редактирования
        self.new_window = QtWidgets.QDialog()  # создает новое базовое окно с последующей настройкой
        self.ui_window = Ui_Dialog()  # определение нового окна
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        sender = self.sender()  # кто отправил последний сигнал в приложении
        if sender.text() == 'Добавить':
            self.ui_window.save_pushButton.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.save_pushButton.clicked.connect(self.edit_current_transaction)


    def add_new_transaction(self):
        title = self.ui_window.le_title_description.text()
        author = self.ui_window.le_author_description.text()
        genre = self.ui_window.le_genre_description.text()
        date_added = self.ui_window.de_date_description.text()
        status = self.ui_window.cb_status_description.currentText()
        price = self.ui_window.le_price_description.text()

        self.db_object.add_transaction_query(title, author, genre, date_added, status, price)
        self.view_data()
        self.new_window.close()


    def edit_current_transaction(self):
        title = self.ui_window.le_title_description.text()
        author = self.ui_window.le_author_description.text()
        genre = self.ui_window.le_genre_description.text()
        date_added = self.ui_window.de_date_description.text()
        status = self.ui_window.cb_status_description.currentText()
        price = self.ui_window.le_price_description.text()
        index = self.ui.tableView.selectedIndexes()[0]  # 0 т.к. редактируется только одна запись
        id = str(self.ui.tableView.model().data(index))  # извлечение id

        self.db_object.edit_transaction_query(title, author, genre, date_added, status, price, id)
        self.view_data()
        self.new_window.close()

    def del_current_transaction(self):
        try:
            index = self.ui.tableView.selectedIndexes()[0]
            id = str(self.ui.tableView.model().data(index))
            self.db_object.delete_transaction_query(id)
            self.view_data()
        except IndexError:
            print('IndexError')



    def filter_lines(self):
        pass

    def analytics_data_base(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)  # передача аргументов системы
    window = Booktrack()  # объект главного окна
    window.show()

    sys.exit(app.exec())
