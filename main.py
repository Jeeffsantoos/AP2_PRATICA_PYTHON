import sqlite3
from criaTabelas import criaTabelaCliente, criaTabelaVendas, criaTabelaMotocicleta, DB_FILE
from AdicionarCampo import AdicionarCliente

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

if __name__ == '__main__':
    criaTabelaCliente()
    criaTabelaMotocicleta()
    criaTabelaVendas()
    #AdicionarCliente("João", "12345678910", "123456789")