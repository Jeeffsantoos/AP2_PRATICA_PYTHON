import sqlite3

# Deleta o cliente no banco de dados
def deletarCliente(id):
    try:
        TABLE_NAME = "Clientes"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            # Verifica se o ID existe na tabela antes de executar a exclusão
            cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE ClienteId = ?", (id,))
            result = cursor.fetchone()

            if result[0] > 0:  # Se o ID existe na tabela
                cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE ClienteId = ?", (id,))
                connection.commit()
                print("\nCliente deletado com sucesso.")
            else:
                print("\nID do cliente não encontrado.")
                
    except Exception as e:
        print("Erro ao deletar o cliente: ", str(e))
        
# Deleta a motocicleta no banco de dados
def deletarMotocicleta(id):
    try:
        TABLE_NAME = "Motocicletas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            # Verifica se o ID existe na tabela antes de executar a exclusão
            cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE MotoId = ?", (id,))
            result = cursor.fetchone()

            if result[0] > 0:  # Se o ID existe na tabela
                cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE MotoId = ?", (id,))
                connection.commit()
                print("\nMotocicleta deletada com sucesso.")
            else:
                print("\nID da moto não encontrado.")
                
    except Exception as e:
        print("Erro ao deletar a motocicleta: ", str(e))

# Deleta a venda no banco de dados
def deletarVenda(id):
    try:
        TABLE_NAME = "Vendas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            # Verifica se o ID existe na tabela antes de executar a exclusão
            cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE VendaId = ?", (id,))
            result = cursor.fetchone()

            if result[0] > 0:  # Se o ID existe na tabela
                cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE VendaId = ?", (id,))
                connection.commit()
                print("\Venda deletada com sucesso.")
            else:
                print("\nID da venda não encontrado.")
    except Exception as e:
        print("Erro ao deletar a venda: ", str(e))
