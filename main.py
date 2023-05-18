import sqlite3
from criaTabelas import criaTabelaCliente, criaTabelaMotocicleta, DB_FILE

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

if __name__ == '__main__':
    criaTabelaCliente()
    criaTabelaMotocicleta()