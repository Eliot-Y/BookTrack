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

        query.exec(f'''CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(40),
                author VARCHAR(30),
                genre VARCHAR(30),
                date_added DATE,
                status VARCHAR(30),
                price INT
        )''')

        query.exec(f'''CREATE TABLE IF NOT EXISTS temp_books(
                    id INTEGER,
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

    def clean_table(self, table_name):
        sql_query = f'DELETE FROM {table_name}'
        self.execute_query_wuth_params(sql_query)

    def create_filtered_table(self, values_dc):  # создает новую таблицу согласно фильтру и отображает её
        self.clean_table('temp_books')
        concat_values = ''
        for k in values_dc:
            concat_values += values_dc[k]

        if concat_values == '':
            sql_query = '''INSERT INTO temp_books SELECT * FROM books'''
            self.execute_query_wuth_params(sql_query)
            return

        sql_query = '''INSERT INTO temp_books SELECT * FROM books'''
        cnt = 0

        for k, v in values_dc.items():
            if v == '':
                continue

            if cnt != 0:
                sql_query += ' AND'
            else:
                sql_query += ' WHERE'

            match k:
                case 'date_from':
                    sql_query += f' date_added >= "{v}"'
                case 'price_bottom':
                    sql_query += f' price >= {v}'
                case 'date_last':
                    sql_query += f' date_added <= "{v}"'
                case 'price_top':
                    sql_query += f' price <= {v}'
                case _:
                    sql_query += f' {k} LIKE ("%{v.capitalize()}%")'
            cnt += 1

        self.execute_query_wuth_params(sql_query)

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
