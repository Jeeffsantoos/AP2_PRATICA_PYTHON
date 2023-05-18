import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'CRUD_AP2'
DB_FILE = ROOT_DIR / DB_NAME

def criaTabelaMotocicleta():
    
    TABLE_NAME = 'Motocicletas'
    
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'modelo VARCHAR,'
        'placa VARCHAR(7),'
        'preco VARCHAR'
        ')'
    )
    
    connection.commit()
    
def criaTabelaCliente():
    
    TABLE_NAME = 'Clientes'
    
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'nome VARCHAR,'
        'cpf VARCHAR(11),'
        'telefone VARCHAR(11)'
        ')'
    )
    
    connection.commit()

    