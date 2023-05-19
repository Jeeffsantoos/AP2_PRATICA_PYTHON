# Projeto de CRUD Python - Cadastro de Motocicletas, Clientes e Vendas

Este projeto consiste em um aplicativo de CRUD (Create, Read, Update, Delete) desenvolvido em Python para o cadastro de motocicletas, clientes e vendas. O objetivo é fornecer um sistema básico para gerenciar informações relacionadas a motocicletas, clientes e suas respectivas vendas.

## Funcionalidades

O aplicativo possui as seguintes funcionalidades:

- Adicionar um cliente ao banco de dados.
- Adicionar uma motocicleta ao banco de dados.
- Adicionar uma venda ao banco de dados.
- Exibir a lista de clientes cadastrados.
- Exibir a lista de motocicletas cadastradas.
- Exibir a lista de vendas registradas.

## Requisitos

- Python 3.x
- SQLite3

## Como executar o projeto

1. Clone este repositório em sua máquina local.

2. Certifique-se de ter o Python instalado em sua máquina.

3. Instale a biblioteca SQLite3, caso não esteja instalada. Você pode usar o seguinte comando:

- pip install pysqlite3

4. Navegue até o diretório do projeto e execute o arquivo `main.py`:

- cd seu-repositorio
- python main.py

5. O aplicativo será executado e você poderá interagir com as funcionalidades disponíveis.

## Observações

- O arquivo de banco de dados `CRUD_AP2.db` será criado automaticamente na mesma pasta onde o arquivo `main.py` está localizado.
- As tabelas necessárias para o funcionamento do aplicativo serão criadas automaticamente quando o programa for executado pela primeira vez.
- Você pode descomentar a linha `#AdicionarCliente("João", "12345678910", "123456789")` no arquivo `main.py` para adicionar um cliente de exemplo ao banco de dados.

Sinta-se à vontade para personalizar e expandir este projeto de acordo com suas necessidades.

Copie o código acima e cole no arquivo README.md do seu repositório no GitHub. O formato Markdown será corretamente interpretado e exibido no GitHub. Certifique-se de salvar o arquivo como README.md para que seja reconhecido como o arquivo de README do seu repositório.
