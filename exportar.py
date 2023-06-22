import pandas as pd
import sqlite3
from datetime import datetime

agora = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

def exportarClientes():
    TABLE_NAME = 'Clientes'
    with sqlite3.connect('CRUD_AP2.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        df = pd.DataFrame(cursor.fetchall(), columns=['id', 'nome', 'cpf', 'telefone'])
        df.to_csv(f'clientes_{agora}.csv', index=False)

def exportarMotocicletas():
    TABLE_NAME = 'Motocicletas'
    with sqlite3.connect('CRUD_AP2.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        df = pd.DataFrame(cursor.fetchall(), columns=['id', 'modelo', 'placa', 'preco'])
        df.to_csv(f'motocicletas_{agora}.csv', index=False)

def exportarVendas():
    TABLE_NAME = 'Vendas'
    with sqlite3.connect('CRUD_AP2.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        df = pd.DataFrame(cursor.fetchall(), columns=['id', 'clienteId', 'motoId', 'data'])
        df.to_csv(f'vendas_{agora}.csv', index=False)