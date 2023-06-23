import sqlite3
from PyQt6 import QtWidgets, QtSql


class Connectdb:
    instance = False

    # def __new__(cls, *args, **kwargs):
    #     if cls.instance:
    #         super.__init__()
    #     instance = True

    def __init__(self):
        super(Connectdb, self).__init__()
        self.db = sqlite3.connect('db_books.db')  # подключение к базе данных
        self.db_curs = self.db.cursor()  # создание курсора для работы с БД
        self.db_curs.execute("""CREATE TABLE IF NOT EXISTS books_lib(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        genre TEXT,
        date_added DATE,
        status TEXT,
        price INTEGER
        )""")

        self.db.commit()

    def add_transaction(self):
        self.db_curs.execute('''INSERT INTO books_lib(title, author, genre, date_added, status, price)
            VALUES( "Над пропастью во ржи2", "Салинджер", "драмма-бейс", "2007.06.21", "Прочитано", "482")''')
        self.db.commit()

    def edit_transaction(self):
        self.db_curs.execute("UPDATE books_lib SET author = 'Мужик', title = 'ват ват ваат' WHERE id = 1")

    def del_transaction(self):
        self.db_curs.execute("DELETE FROM books_lib WHERE id = 2")
        self.db.commit()

    def get_sum_price(self):
        sum_price = self.db_curs.execute('SELECT SUM(price) FROM books_lib').fetchone()
        return sum_price

    def get_sum_amount(self):
        sum_amount = self.db_curs.execute('SELECT COUNT(id) FROM books_lib').fetchone()
        return sum_amount

    def show_table(self):
        self.db_curs.execute('SELECT * FROM books_lib')
        return self.db_curs.fetchall()

    def filter_table(self):
        self.db_curs.execute('SELECT * FROM books_lib WHERE')
        return self.db_curs.fetchall()
