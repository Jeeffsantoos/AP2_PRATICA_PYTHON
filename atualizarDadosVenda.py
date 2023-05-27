import sqlite3

def atualizarDataVenda(VendaId, data):
    try:
        TABLE_NAME = "Vendas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET data = ? '
                'WHERE VendaID = ?',
                (data, VendaId)
            )

            connection.commit()
            print("\nVenda atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Venda: ", str(e))

def atualizarIdCliente(VendaId , idCliente):
    try:
        TABLE_NAME = "Vendas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET cliente_id = ? '
                'WHERE VendaId = ?',
                (idCliente, VendaId)
            )

            connection.commit()
            print("\nVenda atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Venda: ", str(e))

def atualizarIdMotoVendida(VendaId, idMoto):
    try:
        TABLE_NAME = "Vendas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET moto_id = ? '
                'WHERE VendaId = ?',
                (idMoto, VendaId)
            )

            connection.commit()
            print("\nVenda atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Venda: ", str(e))
        
