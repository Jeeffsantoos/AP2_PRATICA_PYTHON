import sqlite3

def atualizarModeloMotocicleta(MotoId, modelo):
    try:
        TABLE_NAME = "Motocicletas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET modelo = ? '
                'WHERE MotoId = ?',
                (modelo, MotoId)
            )

            connection.commit()
            print("Motocicleta atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Motocicleta: ", str(e))

def atualizarPlacaMotocicleta(MotoId , placa):
    try:
        TABLE_NAME = "Motocicletas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET placa = ? '
                'WHERE MotoId = ?',
                (placa, MotoId)
            )

            connection.commit()
            print("Motocicleta atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Motocicleta: ", str(e))

def atualizarPrecoMotocicleta(MotoId, preco):
    try:
        TABLE_NAME = "Motocicletas"

        with sqlite3.connect("CRUD_AP2.db") as connection:
            cursor = connection.cursor()

            cursor.execute(
                f'UPDATE {TABLE_NAME} '
                'SET preco = ? '
                'WHERE MotoId = ?',
                (preco, MotoId)
            )

            connection.commit()
            print("Motocicleta atualizada com sucesso.")
            
    except Exception as e:
        print("Erro ao atualizar a Motocicleta: ", str(e))
        
