import sqlite3
from main import DB_FILE

TABLE_NAME = 'Motocicletas'

with sqlite3.connect(DB_FILE) as connection:
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM {TABLE_NAME}')

    for row in cursor.fetchall():
        _id, modelo, placa, preco = row
        print(_id, modelo, placa, preco)
