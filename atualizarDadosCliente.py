import sqlite3

def atualizarNomeCliente(id , nome):
    try:
        TABLE_NAME = "Clientes"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            # Checa se o cliente existe
            cursor.execute(
                f'SELECT * FROM {TABLE_NAME} '
                'WHERE ClienteId = ?',
                (id,)
            )

            cliente = cursor.fetchone()

            if cliente is None:
                print("\nCliente não encontrado.")
                return
            
            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET nome = ? '
                'WHERE ClienteId = ?',
                (nome, id)
            )

            connection.commit()
            print("\nCliente atualizado com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar o cliente: ", str(e))

def atualizarCpfCliente(id , cpf):
    try:
        TABLE_NAME = "Clientes"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()
            
            # Checa se o cliente existe
            cursor.execute(
                f'SELECT * FROM {TABLE_NAME} '
                'WHERE ClienteId = ?',
                (id,)
            )

            cliente = cursor.fetchone()

            if cliente is None:
                print("\nCliente não encontrado.")
                return
            
            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET cpf = ? '
                'WHERE ClienteId = ?',
                (cpf, id)
            )

            connection.commit()
            print("\nCliente atualizado com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar o cliente: ", str(e))

def atualizarTelefoneCliente(id, telefone):
    try:
        TABLE_NAME = "Clientes"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            # Checa se o cliente existe
            cursor.execute(
                f'SELECT * FROM {TABLE_NAME} '
                'WHERE ClienteId = ?',
                (id,)
            )

            cliente = cursor.fetchone()

            if cliente is None:
                print("\nCliente não encontrado.")
                return
            
            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET telefone = ? '
                'WHERE ClienteId = ?',
                (telefone, id)
            )

            connection.commit()
            print("\nCliente atualizado com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar o cliente: ", str(e))
        
