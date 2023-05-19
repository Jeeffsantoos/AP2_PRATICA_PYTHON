import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'CRUD_AP2.db'
DB_FILE = ROOT_DIR / DB_NAME

def criaTabelaMotocicleta():
    try:
        
        TABLE_NAME = 'Motocicletas'
        
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
                '('
                'MotoId INTEGER PRIMARY KEY AUTOINCREMENT,'
                'modelo VARCHAR NOT NULL,'
                'placa VARCHAR(7) NOT NULL,'
                'preco VARCHAR NOT NULL'
                ')'
            )
            
            connection.commit()
            print("O arquivo do banco de dados foi criado com sucesso.")
    except Exception as e:
        print("Erro ao criar o arquivo do banco de dados (Motocicletas): ", str(e))
    
def criaTabelaCliente():
    try:

        TABLE_NAME = 'Clientes'
        
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
                '('
                'ClienteId INTEGER PRIMARY KEY AUTOINCREMENT,'
                'nome VARCHAR(255) NOT NULL,'
                'cpf VARCHAR(11) NOT NULL,'
                'telefone VARCHAR(11) NOT NULL'
                ')'
            )
            
            connection.commit()
            print("O arquivo do banco de dados foi criado com sucesso.")
    except Exception as e:
        print("Erro ao criar o arquivo do banco de dados (Clientes): ", str(e))

def criaTabelaVendas():
    try:

        TABLE_NAME = "Vendas"

        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
                '('
                'VendaId INTEGER PRIMARY KEY AUTOINCREMENT,'
                'cliente_id INTEGER NOT NULL,'
                'moto_id INTEGER NOT NULL,'
                'data DATE NOT NULL,'
                'FOREIGN KEY (cliente_id) REFERENCES Clientes(ClienteId),'
                'FOREIGN KEY (moto_id) REFERENCES Motocicletas(MotoId)'
                ')'
            )

            connection.commit()
            print("O arquivo do banco de dados foi criado com sucesso.")
    except Exception as e:
        print("Erro ao criar o arquivo do banco de dados (Vendas): ", str(e))
