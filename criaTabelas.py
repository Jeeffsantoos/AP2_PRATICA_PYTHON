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
            'id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,'
            'modelo VARCHAR NOT NULL,'
            'placa VARCHAR(7) NOT NULL,'
            'preco VARCHAR NOT NULL'
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
            'id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,'
            'nome VARCHAR NOT NULL,'
            'cpf VARCHAR(11) NOT NULL,'
            'telefone VARCHAR(11) NOT NULL'
            ')'
        )
        
        connection.commit()

    