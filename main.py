import mysql.connector

# Função para conectar ao banco de dados
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="nome_do_banco"
    )

# Função para criar uma tabela de motos
def criar_tabela_motos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS motos (id INT AUTO_INCREMENT PRIMARY KEY, marca VARCHAR(255), modelo VARCHAR(255), ano INT)")
    conn.close()

# Função para inserir uma moto na tabela
def inserir_moto():
    conn = conectar()
    cursor = conn.cursor()
    marca = input("Digite a marca da moto: ")
    modelo = input("Digite o modelo da moto: ")
    ano = input("Digite o ano da moto: ")
    sql = "INSERT INTO motos (marca, modelo, ano) VALUES (%s, %s, %s)"
    valores = (marca, modelo, ano)
    cursor.execute(sql, valores)
    conn.commit()
    print("Moto inserida com sucesso!")
    conn.close()

# Função para listar todas as motos
def listar_motos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM motos")
    motos = cursor.fetchall()
    if not motos:
        print("Não há motos cadastradas.")
    else:
        for moto in motos:
            print(f"ID: {moto[0]}, Marca: {moto[1]}, Modelo: {moto[2]}, Ano: {moto[3]}")
    conn.close()

# Função para atualizar os dados de uma moto
def atualizar_moto():
    conn = conectar()
    cursor = conn.cursor()
    id_moto = input("Digite o ID da moto que deseja atualizar: ")
    marca = input("Digite a nova marca da moto: ")
    modelo = input("Digite o novo modelo da moto: ")
    ano = input("Digite o novo ano da moto: ")
    sql = "UPDATE motos SET marca=%s, modelo=%s, ano=%s WHERE id=%s"
    valores = (marca, modelo, ano, id_moto)
    cursor.execute(sql, valores)
    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhuma moto encontrada com esse ID.")
    else:
        print("Moto atualizada com sucesso!")
    conn.close()

# Função para excluir uma moto
def excluir_moto():
    conn = conectar()
    cursor = conn.cursor()
    id_moto = input("Digite o ID da moto que deseja excluir: ")
    sql = "DELETE FROM motos WHERE id=%s"
    valores = (id_moto,)
    cursor.execute(sql, valores)
    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhuma moto encontrada com esse ID.")
    else:
        print("Moto excluída com sucesso!")
    conn.close()

# Função para exibir o menu e processar as opções
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Criar tabela de motos")
        print("2 - Inserir uma moto")
        print("3 - Listar motos")
        print("4 - Atualizar moto")
        print("5 - Excluir moto")
        print("0 - Sair do programa")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            criar_tabela_motos()
        elif opcao == "2":
            inserir_moto()
        elif opcao == "3":
            listar_motos()
        elif opcao == "4":
            atualizar_moto()
        elif opcao == "5":
            excluir_moto()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Comando Inválido!")

menu()