import sqlite3
from typing import List, Any
from PyQt6 import QtWidgets, QtSql


class DataB:
    def __init__(self):
        super(DataB, self).__init__()

    def create_connection(self):  # создание подключения к бд
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')  # назначение sql и создание объекта
        db.setDatabaseName('books_db.db')
        if not db.open():  # проверка на подключение
            QtWidgets.QMessageBox.critical(None, "Не удалось подключиться к базе данных", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()  # объект для sql запросов
        query.exec('''CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(40),
            author VARCHAR(30),
            genre VARCHAR(30),
            date_added VARCHAR(12),
            status VARCHAR(30),
            price INT
        )''')
        return True

    def execute_query_wuth_params(self, sql_query, values=None):  # вставляет значения в sql-запрос и исполняет
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)  # подготовка sql запроса

        if values is not None:  # если есть параметры, добавляем в запрос
            for value in values:
                query.addBindValue(value)

        query.exec()
        query.first()  # указатель на начало результата
        return query

    def add_transaction_query(self, title, author, genre, date_added, status, price):  # добавление записи
        sql_query = 'INSERT INTO books (title, author, genre, date_added, status, price) VALUES (?, ?, ?, ?, ?, ?)'
        self.execute_query_wuth_params(sql_query, [title, author, genre, date_added, status, price])

    def edit_transaction_query(self, title, author, genre, date_added, status, price, id):  # редактирование записи + id
        sql_query = '''UPDATE books SET title=?, author=?, genre=?, date_added=?, status=?, price=?
                       WHERE id = ?'''
        self.execute_query_wuth_params(sql_query, [title, author, genre, date_added, status, price, id])

    def delete_transaction_query(self, id):  # удаление записи
        sql_query = '''DELETE FROM books WHERE id = ?'''
        self.execute_query_wuth_params(sql_query, [id])

    def get_line_data(self, id):
        sql_query = f'SELECT * FROM books WHERE id={id}'
        query = self.execute_query_wuth_params(sql_query)

        if query.isActive():  # проверка активен ли запрос
            line_date = []
            # извлечение данных по названию столбцов
            for i in range(1, 7):
                line_date.append(query.value(i))

            return line_date
        else:
            print("Запрос не активен")
            return False

    def get_count_lines(self):
        sql_query = 'SELECT COUNT(id) FROM books'
        query = self.execute_query_wuth_params(sql_query)
        return query.value(0)

    def get_sum_price(self):
        sql_query = 'SELECT SUM(price) FROM books'
        query = self.execute_query_wuth_params(sql_query)
        return query.value(0)
