import sqlite3
from main import DB_FILE

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

TABLE_NAME = 'Clientes'
cursor.execute(f'SELECT * FROM {TABLE_NAME}')


for row in cursor.fetchall():
    _id, nome, cpf, telefone = row
    print(_id, nome, telefone, cpf)
    
cursor.close()
connection.close()