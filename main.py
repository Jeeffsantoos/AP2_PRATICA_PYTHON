from criaTabelas import criaTabelaCliente, criaTabelaVendas, criaTabelaMotocicleta
from adicionarCampo import adicionarCliente, adicionarMotocicleta, adicionarVenda
from exibirDados import exibirClientes, exibirMotocicletas, exibirVendas
from atualizarDadosCliente import atualizarCpfCliente, atualizarNomeCliente, atualizarTelefoneCliente
from atualizarDadosMotocicleta import atualizarModeloMotocicleta, atualizarPlacaMotocicleta, atualizarPrecoMotocicleta
from atualizarDadosVenda import atualizarDataVenda, atualizarIdCliente, atualizarIdVendidaVenda


if __name__ == '__main__':
    criaTabelaCliente()
    criaTabelaMotocicleta()
    criaTabelaVendas()
