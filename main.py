from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from PyQt6.QtSql import QSqlTableModel
from ui_main import Ui_MainWindow
from connection import DataB
from ui_add_ed_window import Ui_Dialog
from datetime import date
import error_window


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

    def view_error(self):
        self.error_window = QtWidgets.QDialog()
        self.ui_error = error_window.Ui_Dialog()
        self.ui_error.setupUi(self.error_window)
        self.error_window.show()

        self.ui_error.ok_pushButton.clicked.connect(self.error_window.close)

    def view_data(self):  # отображение данных из БД
        self.model = QSqlTableModel(self)
        self.model.setTable('books')  # соединение с таблицей
        self.model.select()  # выбрать данные
        self.ui.tableView.setModel(self.model)  # отображение таблицы
        # установка количества книг и общей цены
        self.ui.total_price_label.setText(str(self.db_object.get_sum_price()) + ' р.')
        self.ui.amount_label.setText(str(self.db_object.get_count_lines()))

    def view_filter_data(self):
        pass

    def open_new_window_ad_ed(self):  # открывает окно ввода и редактирования
        self.new_window = QtWidgets.QDialog()  # создает новое базовое окно с последующей настройкой
        self.ui_window = Ui_Dialog()  # определение нового окна
        self.ui_window.setupUi(self.new_window)

        sender = self.sender()  # кто отправил последний сигнал в приложении

        if sender.text() == 'Добавить':
            set_data_obj = self.ui_window.de_date_description.date()  # объект класса дата
            today_date = date.today()
            set_data_obj.setDate(today_date.year, today_date.month, today_date.day)
            self.ui_window.de_date_description.setDate(set_data_obj)  # устанавливаем текущую дату

            self.new_window.show()
            self.ui_window.save_pushButton.clicked.connect(self.add_new_transaction)
        else:
            # проверка на выделение id, окно выведется, если выделена одна запись
            index = self.ui.tableView.selectedIndexes()
            if len(index) != 1:
                self.view_error()
                return

            book_status_dc = {'В планах': 0, 'Брошено': 1, 'В процессе': 2, 'Прочитано': 3}

            # настроить отображение старых данных
            id = str(self.ui.tableView.model().data(index[0]))
            data_lst = self.db_object.get_line_data(id)  # получение значений записи с переданным id
            line_date = [int(c) for c in data_lst[3].split('.')[::-1]]

            self.ui_window.le_title_description.setText(data_lst[0])
            self.ui_window.le_author_description.setText(data_lst[1])
            self.ui_window.le_genre_description.setText(data_lst[2])
            set_data_obj = self.ui_window.de_date_description.date()  # объект класса дата
            set_data_obj.setDate(*line_date)  # значение объекта
            self.ui_window.de_date_description.setDate(set_data_obj)  # устанавливаем новую дату
            # меняем местами два статуса, основной ставится в позицию ноль, а его позицию занимает статус по умолчанию
            self.ui_window.cb_status_description.setItemText(book_status_dc[data_lst[4]], 'В планах')
            self.ui_window.cb_status_description.setItemText(0, data_lst[4])
            self.ui_window.le_price_description.setText(str(data_lst[5]))

            self.new_window.show()
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
        if len(self.ui.tableView.selectedIndexes()) == 0:
            self.view_error()
            return

        index = self.ui.tableView.selectedIndexes()
        for i in index:
            id = (self.ui.tableView.model().data(i))
            self.db_object.delete_transaction_query(id)
        self.view_data()

    def filter_lines(self):
        pass

    def analytics_data_base(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)  # передача аргументов системы
    window = Booktrack()  # объект главного окна
    window.show()
    sys.exit(app.exec())
