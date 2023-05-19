import sqlite3

def ExibirClientes():

    TABLE_NAME = 'Clientes'

    with sqlite3.connect('CRUD_AP2.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        for row in cursor.fetchall():
            _id, nome, cpf, telefone = row
            print(_id, nome, telefone, cpf)

def ExibirMotocicletas():

    TABLE_NAME = 'Motocicletas'

    with sqlite3.connect('CRUD_AP2.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        for row in cursor.fetchall():
            _id, modelo, placa, preco = row
            print(_id, modelo, placa, preco)

def ExibirVendas():
    
        TABLE_NAME = 'Vendas'
    
        with sqlite3.connect('CRUD_AP2.db') as connection:
            cursor = connection.cursor()
    
            cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    
            for row in cursor.fetchall():
                _id, clienteId, motoId, data = row
                print(_id, clienteId, motoId, data)