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
            print("Venda atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Venda: ", str(e))

def atualizarIdCliente(VendaId , idCliente):
    try:
        TABLE_NAME = "Vendas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET id_cliente = ? '
                'WHERE VendaId = ?',
                (idCliente, VendaId)
            )

            connection.commit()
            print("Venda atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Venda: ", str(e))

def atualizarIdVendidaVenda(VendaId, idVenda):
    try:
        TABLE_NAME = "Vendas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET id_Venda = ? '
                'WHERE VendaId = ?',
                (idVenda, VendaId)
            )

            connection.commit()
            print("Venda atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Venda: ", str(e))
        
