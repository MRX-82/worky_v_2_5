"""
Worky data base
"""

import sqlite3 as sql
connect_data_base = sql.connect('worky_DataBase.db')
cursor = connect_data_base.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
Login TEXT NOT NULL,
counter_dst INTEGER,
counter_odo INTEGER
)
''')

class Counter:
    """
    This is class for save and load data counter
    """
    def __init__(self, Login, counter_dst, counter_odo):
        self.Login = Login
        self.counter_dst = counter_dst
        self.counter_odo = counter_odo

    def save(self):
        cursor.execute(
            'INSERT INTO Users(Login, counter_dst, counter_odo) VALUES(?,?, ?)',
            (self.Login, self.counter_dst, self.counter_odo)
        )
        connect_data_base.commit()
        connect_data_base.close()

    def download(self):
        cursor.execute('SELEST * FROM Users')
        counter = cursor.fetchall()
        return counter

    def update(self):
        cursor.execute(
            'UPDATE Users SET counter_dst=?, counter_odo=? WHERE Login=?',
            (self.counter_dst, self.counter_odo, 'Shock')
        )
        connect_data_base.commit()
        connect_data_base.close()