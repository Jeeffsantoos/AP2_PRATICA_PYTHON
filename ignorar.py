import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'CRUD_AP2'
DB_FILE = ROOT_DIR / DB_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

sql = (
    f'INSERT INTO {TABLE_NAME} (name, endereco, cpf, telefone) '
    'VALUES (?,?,?,?)'
)

# CREATE
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'endereco TEXT,'
    'cpf TEXT,'
    'telefone TEXT'
    ')'
)
connection.commit()

cursor.execute(sql, ['Jefferson', 'Duque de Caxias', 150, 150])
connection.commit()

cursor.close()
connection.close()

if __name__ == '__main__':
    print(sql)