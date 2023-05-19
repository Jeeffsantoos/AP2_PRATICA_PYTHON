import sqlite3

# Deleta o cliente no banco de dados
def DeletarCliente(id):
    try:
        TABLE_NAME = "Clientes"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"DELETE FROM {TABLE_NAME} WHERE id = ?",
                (id,),
            )

            connection.commit()
            print("Cliente deletado com sucesso.")
    except Exception as e:
        print("Erro ao deletar o cliente: ", str(e))

# Deleta a motocicleta no banco de dados
def DeletarMotocicleta(id):
    try:
        TABLE_NAME = "Motocicletas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"DELETE FROM {TABLE_NAME} WHERE id = ?",
                (id,),
            )

            connection.commit()
            print("Motocicleta deletada com sucesso.")
    except Exception as e:
        print("Erro ao deletar a motocicleta: ", str(e))

# Deleta a venda no banco de dados
def DeletarVenda(id):
    try:
        TABLE_NAME = "Vendas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()
            
            cursor.execute(
                f"DELETE FROM {TABLE_NAME} WHERE id = ?",
                (id,),
            )

            connection.commit()
            print("Venda deletada com sucesso.")
    except Exception as e:
        print("Erro ao deletar a venda: ", str(e))
