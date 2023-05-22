import sqlite3

# Deleta o cliente no banco de dados
def deletarCliente(id):
    try:
        TABLE_NAME = "Clientes"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                # Está vendo o id?
                # era pra ele estar como ClienteId (Nome que demos para ele)
                f"DELETE FROM {TABLE_NAME} WHERE ClienteId = ?",
                (id,),
            )

            connection.commit()
            print("Cliente deletado com sucesso.")
    except Exception as e:
        print("Erro ao deletar o cliente: ", str(e))

# Deleta a motocicleta no banco de dados
def deletarMotocicleta(id):
    try:
        TABLE_NAME = "Motocicletas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"DELETE FROM {TABLE_NAME} WHERE MotoId = ?",
                (id,),
            )

            connection.commit()
            print("Motocicleta deletada com sucesso.")
    except Exception as e:
        print("Erro ao deletar a motocicleta: ", str(e))

# Deleta a venda no banco de dados
def deletarVenda(id):
    try:
        TABLE_NAME = "Vendas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()
            
            cursor.execute(
                f"DELETE FROM {TABLE_NAME} WHERE VendaId = ?",
                (id,),
            )

            connection.commit()
            print("Venda deletada com sucesso.")
    except Exception as e:
        print("Erro ao deletar a venda: ", str(e))
