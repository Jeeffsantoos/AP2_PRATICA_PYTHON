from criaTabelas import criaTabelaCliente, criaTabelaVendas, criaTabelaMotocicleta
from adicionarCampo import AdicionarCliente, AdicionarMotocicleta, AdicionarVenda
from exibirDados import exibirClientes, exibirMotocicletas, exibirVendas
from deletarCampo import deletarCliente, deletarMotocicleta, deletarVenda

if __name__ == '__main__':
    criaTabelaCliente()
    criaTabelaMotocicleta()
    criaTabelaVendas()
    #AdicionarCliente("João", "12345678910", "123456789")