# Função para exibir o menu e processar as opções

from criaTabelas import criaTabelaCliente, criaTabelaVendas, criaTabelaMotocicleta
from adicionarCampo import adicionarCliente, adicionarMotocicleta, adicionarVenda
from deletarCampo import deletarCliente, deletarMotocicleta, deletarVenda
from exibirDados import exibirClientes, exibirMotocicletas, exibirVendas
from atualizarDadosCliente import atualizarCpfCliente, atualizarNomeCliente, atualizarTelefoneCliente
from atualizarDadosMotocicleta import atualizarModeloMotocicleta, atualizarPlacaMotocicleta, atualizarPrecoMotocicleta
from atualizarDadosVenda import atualizarDataVenda, atualizarIdCliente, atualizarIdVendidaVenda


def menu():
   while True:
       print("\n MENU")
       print("1 - Criar tabelas")
       print("2 - Adiconar campo")
       print("3 - Exibir dados")
       print("4 - Atualizar dados dos clientes")
       print("5 - Atualizar motos")
       print("6 - Atualizar vendas")
       print("0 - Sair do programa")
       opcao = input("Digite o número da opção desejada: ")


       if opcao == "1":
           criaTabelas()
       elif opcao == "2":
           adicionarCampo()
       elif opcao == "3":
           exibirDados()
       elif opcao == "4":
           atualizarDadosCliente()
       elif opcao == "5":
           atualizarDadosMotocicleta()
       elif opcao == "6":
           atualizarDadosVenda()
       elif opcao == "0":
           print("Saindo do programa...")
           break
       else:
           print("Comando Inválido!")


def criaTabelas():
   while True:
       print("\n--- Qual tabela você deseja criar? ---")
       print("1 - Criar tabela de clientes")
       print("2 - Criar tabela de vendas")
       print("3 - Criar tabela de motocicletas")
       print("0 - Voltar ao menu anterior")
       opcao = input("Digite o número da opção desejada: ")


       if opcao == "1":
           criaTabelaCliente()
       elif opcao == "2":
           criaTabelaVendas()
       elif opcao == "3":
           criaTabelaMotocicleta()
       elif opcao == "0":
           break
       else:
           print("Comando Inválido!")


def adicionarCampo():
   while True:
       print("--- O que você deseja adicionar? ---")
       print("1 - Adicionar cliente")
       print("2 - Adicionar motocicleta")
       print("3 - Adicionar venda")
       print("0 - Voltar ao menu anterior")
       opcao = input("Digite o número da opção desejada: ")


       if opcao == "1":
           adicionarCliente()
       elif opcao == "2":
           adicionarMotocicleta()
       elif opcao == "3":
           adicionarVenda()
       elif opcao == "0":
           break
       else:
           print("Comando Inválido!")


def deletarCampo():
   while True:
       print("\n--- O que você deseja deletar? ---")
       print("1 - Deletar cliente")
       print("2 - Deletar motocicleta")
       print("3 - Deletar venda")
       print("0 - Voltar ao menu anterior")
       opcao = input("Digite o número da opção desejada: ")


       if opcao == "1":
           deletarCliente()
       elif opcao == "2":
           deletarMotocicleta()
       elif opcao == "3":
           deletarVenda()
       elif opcao == "0":
           break
       else:
           print("Comando Inválido!")


def exibirDados():
   while True:
       print("\n--- Quais dados você deseja exibir? ---")
       print("1 - Exibir lista de clientes")
       print("2 - Exibir dados das motocicletas")
       print("3 - Exibir vendas efetuadas")
       print("0 - Voltar ao menu anterior")
       opcao = input("Digite o número da opção desejada: ")


       if opcao == "1":
           exibirClientes()
       elif opcao == "2":
           exibirMotocicletas()
       elif opcao == "3":
           exibirVendas()
       elif opcao == "0":
           break
       else:
           print("Comando Inválido!")


def atualizarDadosCliente():
   while True:
       print("\n--- O que você deseja atualizar? ---")
       print("1 - Atualizar CPF do cliente")
       print("2 - Atualizar nome do cliente")
       print("3 - Atualizar telefone do cliente")
       print("0 - Voltar ao menu anterior")
       opcao = input("Digite o número da opção desejada: ")


       if opcao == "1":
           atualizarCpfCliente()
       elif opcao == "2":
           atualizarNomeCliente()
       elif opcao == "3":
           atualizarTelefoneCliente()
       elif opcao == "0":
           break
       else:
           print("Comando Inválido!")


def atualizarDadosMotocicleta():
   while True:
       print("\n--- O que você deseja atualizar? ---")
       print("1 - Atualizar preço da motocicleta")
       print("2 - Atualizar modelo da motocicleta")
       print("3 - Atualizar placa da motocicleta")
       print("0 - Voltar ao menu anterior")
       opcao = input("Digite o número da opção desejada: ")


       if opcao == "1":
           atualizarPrecoMotocicleta()
       elif opcao == "2":
           atualizarModeloMotocicleta()
       elif opcao == "3":
           atualizarPlacaMotocicleta()
       elif opcao == "0":
           break
       else:
           print("Comando Inválido!")


def atualizarDadosVenda():
   while True:
       print("\n--- O que você deseja atualizar? ---")
       print("1 - Atualizar data da venda")
       print("2 - Atualizar ID do cliente")
       print("3 - Atualizar ID da venda")
       print("0 - Voltar ao menu anterior")
       opcao = input("Digite o número da opção desejada: ")


       if opcao == "1":
           atualizarDataVenda()
       elif opcao == "2":
           atualizarIdCliente()
       elif opcao == "3":
           atualizarIdVendidaVenda()
       elif opcao == "0":
           break
       else:
           print("Comando Inválido!")