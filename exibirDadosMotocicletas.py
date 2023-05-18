import sqlite3
from main import DB_FILE

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

TABLE_NAME = 'Motocicletas'
cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id, modelo, placa, preco = row
    print(_id, modelo, placa, preco)
    
cursor.close()
connection.close()