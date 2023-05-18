import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'CRUD_AP2'
DB_FILE = ROOT_DIR / DB_NAME

def criaTabelaMotocicleta():
    
    TABLE_NAME = 'Motocicletas'
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'modelo TEXT,'
        'placa TEXT,'
        'preco TEXT'
        ')'
    )
    
    connection.commit()
    cursor.close()
    connection.close()
    
def criaTabelaCliente():
    
    TABLE_NAME = 'Clientes'
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'nome TEXT,'
        'cpf TEXT,'
        'telefone TEXT'
        ')'
    )
    
    connection.commit()
    cursor.close()
    connection.close()
    