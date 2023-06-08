from criaTabelas import criaTabelaCliente, criaTabelaVendas, criaTabelaMotocicleta
from adicionarCampo import adicionarCliente, adicionarMotocicleta, adicionarVenda
from deletarCampo import deletarCliente, deletarMotocicleta, deletarVenda
from exibirDados import exibirClientes, exibirMotocicletas, exibirVendas
from atualizarDadosCliente import (
    atualizarCpfCliente,
    atualizarNomeCliente,
    atualizarTelefoneCliente,
)
from atualizarDadosMotocicleta import (
    atualizarModeloMotocicleta,
    atualizarPlacaMotocicleta,
    atualizarPrecoMotocicleta,
)
from atualizarDadosVenda import (
    atualizarDataVenda,
    atualizarIdCliente,
    atualizarIdMotoVendida,
)


def menu():
    while True:
        print("\nMENU\n")
        print("1 - Adicionar campo")
        print("2 - Deletar Campo")
        print("3 - Exibir dados")
        print("4 - Atualizar dados dos clientes")
        print("5 - Atualizar motos")
        print("6 - Atualizar vendas")
        print("0 - Sair do programa\n")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            adicionarCampo()
            break
        elif opcao == "2":
            deletarCampo()
            break
        elif opcao == "3":
            exibirDados()
            break
        elif opcao == "4":
            atualizarDadosCliente()
            break
        elif opcao == "5":
            atualizarDadosMotocicleta()
            break
        elif opcao == "6":
            atualizarDadosVenda()
            break
        elif opcao == "0":
            print("\nSaindo do programa...")
            break
        else:
            print("\nComando Inválido!")

# Faz a criação das tabelas
def criaTabelas():
    criaTabelaCliente()
    criaTabelaVendas()
    criaTabelaMotocicleta()

# Opção de adicionar campo
def adicionarCampo():
    while True:
        print("\n--- O que você deseja adicionar? ---")
        print("1 - Adicionar cliente")
        print("2 - Adicionar motocicleta")
        print("3 - Adicionar venda")
        print("0 - Voltar ao menu anterior\n")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nome = input("\nDigite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            adicionarCliente(nome, cpf, telefone)
        elif opcao == "2":
            modelo = input("Digite o modelo da motocicleta: ")
            placa = input("Digite a placa da motocicleta: ")
            preco = input("Digite o preço da motocicleta: ")
            adicionarMotocicleta(modelo, placa, preco)
        elif opcao == "3":
            clienteId = input("Digite o ID do cliente: ")
            motoId = input("Digite o ID da motocicleta: ")
            data = input("Digite a data da venda: ")
            adicionarVenda(clienteId, motoId, data)
        elif opcao == "0":
            menu()
            break
        else:
            print("\nComando Inválido!")

# Opção de deletar campo
def deletarCampo():
    while True:
        print("\n--- O que você deseja deletar? ---")
        print("1 - Deletar cliente")
        print("2 - Deletar motocicleta")
        print("3 - Deletar venda")
        print("0 - Voltar ao menu anterior\n")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            cliente_id = int(input("Digite o ID do cliente que deseja deletar: "))
            deletarCliente(cliente_id)
        elif opcao == "2":
            motocicleta_id = int(
                input("Digite o ID da motocicleta que deseja deletar: ")
            )
            deletarMotocicleta(motocicleta_id)
        elif opcao == "3":
            venda_id = int(input("Digite o ID da venda que deseja deletar: "))
            deletarVenda(venda_id)
        elif opcao == "0":
            menu()
            break
        else:
            print("\nComando Inválido!")

# Opção de exibir dados
def exibirDados():
    while True:
        print("\n--- Quais dados você deseja exibir? ---")
        print("1 - Exibir lista de clientes")
        print("2 - Exibir dados das motocicletas")
        print("3 - Exibir vendas efetuadas")
        print("0 - Voltar ao menu anterior\n")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            exibirClientes()
        elif opcao == "2":
            exibirMotocicletas()
        elif opcao == "3":
            exibirVendas()
        elif opcao == "0":
            menu()
            break
        else:
            print("\nComando Inválido!")

# Opção de atualizar os dados do cliente
def atualizarDadosCliente():
    while True:
        print("\n--- O que você deseja atualizar? ---")
        print("1 - Atualizar CPF do cliente")
        print("2 - Atualizar nome do cliente")
        print("3 - Atualizar telefone do cliente")
        print("0 - Voltar ao menu anterior\n")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            id_cliente = int(input("Digite o ID do cliente que deseja atualizar: "))
            cpf_cliente = input("Digite o novo CPF do cliente: ")
            atualizarCpfCliente(id_cliente, cpf_cliente)
        elif opcao == "2":
            id_cliente = int(input("Digite o ID do cliente que deseja atualizar: "))
            nome_cliente = input("Digite o novo nome do cliente: ")
            atualizarNomeCliente(id_cliente, nome_cliente)
        elif opcao == "3":
            id_cliente = int(input("Digite o ID do cliente que deseja atualizar: "))
            telefone_cliente = input("Digite o novo telefone do cliente: ")
            atualizarTelefoneCliente(id_cliente, telefone_cliente)
        elif opcao == "0":
            menu()
            break
        else:
            print("\nComando Inválido!")

# Opção de atualizar os dados das motos
def atualizarDadosMotocicleta():
    while True:
        print("\n--- O que você deseja atualizar? ---")
        print("1 - Atualizar preço da motocicleta")
        print("2 - Atualizar modelo da motocicleta")
        print("3 - Atualizar placa da motocicleta")
        print("0 - Voltar ao menu anterior\n")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            id_moto = int(input("Digite o ID da motocicleta que deseja atualizar:"))
            preco_moto = float(input("Digite o novo preço da motocicleta: "))
            atualizarPrecoMotocicleta(id_moto, preco_moto)
        elif opcao == "2":
            id_moto = int(input("Digite o ID da motocicleta que deseja atualizar:"))
            modelo_moto = input("Digite o novo modelo da motocicleta: ")    
            atualizarModeloMotocicleta(id_moto, modelo_moto)
        elif opcao == "3":
            id_moto = int(input("Digite o ID da motocicleta que deseja atualizar:"))
            placa_moto = input("Digite a nova placa da motocicleta: ")
            atualizarPlacaMotocicleta(id_moto, placa_moto)
        elif opcao == "0":
            menu()
            break
        else:
            print("\nComando Inválido!")

# Opção de atualizar os dados das vendas
def atualizarDadosVenda():
    while True:
        print("\n--- O que você deseja atualizar? ---")
        print("1 - Atualizar data da venda")
        print("2 - Atualizar ID do cliente")
        print("3 - Atualizar ID da venda")
        print("0 - Voltar ao menu anterior\n")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            id_venda = int(input("Digite o ID da venda que deseja atualizar: "))
            data_venda = input("Digite a nova data da venda: ")
            atualizarDataVenda(id_venda, data_venda)
        elif opcao == "2":
            id_venda = int(input("Digite o ID da venda que deseja atualizar: "))
            id_cliente = input("Digite o novo ID do cliente: ")
            atualizarIdCliente(id_venda, id_cliente)
        elif opcao == "3":
            id_venda = int(input("Digite o ID da venda que deseja atualizar: "))
            id_motovendida = input("Digite o novo ID da venda: ")
            atualizarIdMotoVendida(id_venda, id_motovendida)
        elif opcao == "0":
            menu()
            break
        else:
            print("\nComando Inválido!")


if __name__ == "__main__":
    criaTabelas()
    menu()
