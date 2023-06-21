import os
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

from exportar import (
    exportarClientes,
    exportarMotocicletas,
    exportarVendas,
)

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        print("\nMENU\n")
        print("1 - Adicionar campo")
        print("2 - Deletar Campo")
        print("3 - Exibir dados")
        print("4 - Atualizar dados dos clientes")
        print("5 - Atualizar motos")
        print("6 - Atualizar vendas")
        print("7 - Exportar dados para CSV")
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
        elif opcao == "7":
            exportarDados()
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
            usuarios = []
            quantidade = int(input("Digite a quantidade de campos que deseja adicionar: "))
            for i in range(quantidade):
                nome = input("\nDigite o nome do cliente: ")
                cpf = input("Digite o CPF do cliente: ")
                telefone = input("Digite o telefone do cliente: ")
                usuarios.append([nome, cpf, telefone])
            limpar_terminal()


            for usuario in usuarios:
                print(f"Nome: {usuario[0]} | CPF: {usuario[1]} | Telefone: {usuario[2]}")

            print("Deseja adicionar todos esses usuários?")
            print("1 - Sim")
            print("2 - Não")
            opcao = input("Digite o número da opção desejada: ")
            if opcao == "1":
                for usuario in usuarios:
                    adicionarCliente(usuario[0], usuario[1], usuario[2])
            else:
                print("Usuários não adicionados!")
                break

        elif opcao == "2":
            moto = []
            quantidade = int(input("Digite a quantidade de campos que deseja adicionar: "))
            for i in range(quantidade):
                modelo = input("\nDigite o modelo da motocicleta: ")
                placa = input("Digite a placa da motocicleta: ")
                preco = input("Digite o preço da motocicleta: ")
                moto.append([modelo, placa, preco])
            limpar_terminal()

            for motos in moto:
                print(f"Modelo: {motos[0]} | Placa: {motos[1]} | Preço: {motos[2]}")
            
            print("Deseja adicionar todos esses usuários?")
            print("1 - Sim")
            print("2 - Não")
            opcao = input("Digite o número da opção desejada: ")
            if opcao == "1":
                for motos in moto:
                    adicionarMotocicleta(motos[0], motos[1], motos[2])
            else:
                print("Motos não adicionadas!")
                break


        elif opcao == "3":
            venda = []
            quantidade = int(input("Digite a quantidade de campos que deseja adicionar: "))
            for i in range(quantidade):
                clienteId = input("Digite o ID do cliente: ")
                motoId = input("Digite o ID da motocicleta: ")
                data = input("Digite a data da venda: ")
                venda.append([clienteId, motoId, data])
            limpar_terminal()

            for vendas in venda:
                print(f"ID do cliente: {vendas[0]} | ID da motocicleta: {vendas[1]} | Data da venda: {vendas[2]}")

            print("Deseja adicionar todos esses usuários?")
            print("1 - Sim")
            print("2 - Não")
            opcao = input("Digite o número da opção desejada: ")
            if opcao == "1":
                for vendas in venda:
                    adicionarVenda(vendas[0], vendas[1], vendas[2])
            else:
                print("Vendas não adicionadas!")
                break

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
            limpar_terminal()
            exibirClientes()
            print("\n Pressione qualquer botão para voltar ao menu")
            input()
        elif opcao == "2":
            limpar_terminal()
            exibirMotocicletas()
            print("\n Pressione qualquer botão para voltar ao menu")
            input()
        elif opcao == "3":
            limpar_terminal()
            exibirVendas()
            print("\n Pressione qualquer botão para voltar ao menu")
            input()
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


# Opção de exportar dados para um CSV

def exportarDados():
    print("\n--- O que você deseja exportar? ---")
    print("1 - Exportar Clientes\n")
    print("2 - Exportar Motocicletas\n")
    print("3 - Exportar Vendas\n")
    print("0 - Voltar ao menu anterior\n")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        exportarClientes()
    elif opcao == 2:
        exportarMotocicletas()
    elif opcao == 3:
        exportarVendas()
    elif opcao == 0:
        menu()
    else:
        print("\nComando Inválido!")

if __name__ == "__main__":
    criaTabelas()
    menu()
