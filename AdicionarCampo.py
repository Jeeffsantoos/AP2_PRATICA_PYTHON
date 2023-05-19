import sqlite3

# Adiciona o cliente no banco de dados
def adicionarCliente(nome, cpf, telefone):
    try:
        TABLE_NAME = "Clientes"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"INSERT INTO {TABLE_NAME} (nome, cpf, telefone) VALUES (?, ?, ?)", 
                (nome, cpf, telefone),
            )

            connection.commit()
            print("Cliente adicionado com sucesso.")
    except Exception as e:
        print("Erro ao adicionar o cliente: ", str(e))

# Adiciona a motocicleta no banco de dados
def adicionarMotocicleta(modelo, placa, preco):
    try:
        TABLE_NAME = "Motocicletas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"INSERT INTO {TABLE_NAME} (modelo, placa, preco) VALUES (?, ?, ?)", 
                (modelo, placa, preco),
            )

            connection.commit()
            print("Motocicleta adicionada com sucesso.")
    except Exception as e:
        print("Erro ao adicionar a motocicleta: ", str(e))

# Adiciona a venda no banco de dados
def adicionarVenda(clienteId, motoId, data):
    try:
        TABLE_NAME = "Vendas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f"INSERT INTO {TABLE_NAME} (clienteId, motoId, data) VALUES (?, ?, ?)",
                (clienteId, motoId, data),
            )

            connection.commit()
            print("Venda adicionada com sucesso.")

    except Exception as e:
        print("Erro ao adicionar a venda: ", str(e))
