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
import os


def excluir_arquivo():
   nome_arquivo = input("Digite o nome do arquivo que deseja excluir: ")
   if os.path.exists(nome_arquivo):
       opcao = input(f'Tem certeza que deseja excluir o arquivo "{nome_arquivo}"? Digite "A" para SIM ou "B" para voltar ao menu anterior: ')
       if opcao == "A":
           os.remove(nome_arquivo)
           print(f'O arquivo "{nome_arquivo}" foi excluído com sucesso.')
       elif opcao == "B":
           print("Voltando ao menu anterior...")
       else:
           print('Opção Inválida! Digite "A" para excluir o arquivo ou "B" para voltar ao menu anterior.')
   else:
       print(f'O arquivo "{nome_arquivo}" não existe.')


def ler_arquivo():
   nome_arquivo = input("Digite o nome do arquivo que deseja ler: ")
   if os.path.exists(nome_arquivo):
       with open(nome_arquivo, 'r') as arquivo:
           conteudo = arquivo.read()
           print(f'Conteúdo do arquivo "{nome_arquivo}":\n{conteudo}')
   else:
       print(f'O arquivo "{nome_arquivo}" não existe.')


def adicionar_arquivo():
   nome_arquivo = input("Digite o nome do arquivo que deseja adicionar: ")
   conteudo = input("Digite o conteúdo do arquivo: ")
   with open(nome_arquivo, 'w') as arquivo:
       arquivo.write(conteudo)
   print(f'O arquivo "{nome_arquivo}" foi adicionado com sucesso.')


def editar_arquivo():
   nome_arquivo = input("Digite o nome do arquivo que deseja editar: ")
   if os.path.exists(nome_arquivo):
       conteudo = input("Digite o novo conteúdo do arquivo: ")
       with open(nome_arquivo, 'w') as arquivo:
           arquivo.write(conteudo)
       print(f'O arquivo "{nome_arquivo}" foi editado com sucesso.')
   else:
       print(f'O arquivo "{nome_arquivo}" não existe.')


def menu():
   nome = input("Digite seu nome: ")
   print(f'Seja bem-vindo, {nome}!')
   while True:
       print("\nO que você deseja fazer?")
       print("1 - Excluir um arquivo")
       print("2 - Ler um arquivo")
       print("3 - Adicionar algum arquivo")
       print("4 - Editar algum arquivo")
       opcao = input("Digite o número da opção desejada: ")


       if opcao == "1":
           excluir_arquivo()
       elif opcao == "2":
           ler_arquivo()
       elif opcao == "3":
           adicionar_arquivo()
       elif opcao == "4":
           editar_arquivo()
       else:
           print("Opção inválida! Digite um número válido.")
           continue


menu()
