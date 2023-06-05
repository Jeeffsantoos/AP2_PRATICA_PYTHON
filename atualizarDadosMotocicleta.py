import sqlite3

def atualizarModeloMotocicleta(MotoId, modelo):
    try:
        TABLE_NAME = "Motocicletas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            # Checa se o cliente existe
            cursor.execute(
                f'SELECT * FROM {TABLE_NAME} '
                'WHERE MotoId = ?',
                (id,)
            )

            moto = cursor.fetchone()

            if moto is None:
                print("\nMotocicleta não encontrada.")
                return

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET modelo = ? '
                'WHERE MotoId = ?',
                (modelo, MotoId)
            )

            connection.commit()
            print("\nMotocicleta atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Motocicleta: ", str(e))

def atualizarPlacaMotocicleta(MotoId , placa):
    try:
        TABLE_NAME = "Motocicletas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            # Checa se o cliente existe
            cursor.execute(
                f'SELECT * FROM {TABLE_NAME} '
                'WHERE MotoId = ?',
                (id,)
            )

            moto = cursor.fetchone()

            if moto is None:
                print("\nMotocicleta não encontrada.")
                return

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET placa = ? '
                'WHERE MotoId = ?',
                (placa, MotoId)
            )

            connection.commit()
            print("\nMotocicleta atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Motocicleta: ", str(e))

def atualizarPrecoMotocicleta(MotoId, preco):
    try:
        TABLE_NAME = "Motocicletas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            # Checa se o cliente existe
            cursor.execute(
                f'SELECT * FROM {TABLE_NAME} '
                'WHERE MotoId = ?',
                (id,)
            )

            moto = cursor.fetchone()

            if moto is None:
                print("\nMotocicleta não encontrada.")
                return

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET preco = ? '
                'WHERE MotoId = ?',
                (preco, MotoId)
            )

            connection.commit()
            print("\nMotocicleta atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Motocicleta: ", str(e))
        
