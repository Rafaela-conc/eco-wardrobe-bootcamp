import os
import mysql.connector
from dotenv import load_dotenv

# Carrega as credenciais salvas no arquivo .env
load_dotenv()


def obter_conexao():
    """Função que conecta ao MySQL na nuvem"""
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT"))
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None


# --- EXEMPLOS DE USO PARA O GRUPO (Pode adaptar nas suas rotas) ---

def cadastrar_roupa(nome, categoria, tamanho, preco, descricao):
    """Exemplo de CREATE (Salvar dados no banco)"""
    conexao = obter_conexao()
    if conexao is None:
        return False

    cursor = conexao.cursor()
    comando = "INSERT INTO roupas (nome, categoria, tamanho, preco, descricao) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, categoria, tamanho, preco, descricao)

    cursor.execute(comando, valores)
    conexao.commit()  # Importante: Confirma a gravação na nuvem!

    id_gerado = cursor.lastrowid
    cursor.close()
    conexao.close()
    return id_gerado


def listar_roupas():
    """Exemplo de READ (Puxar dados do banco)"""
    conexao = obter_conexao()
    if conexao is None:
        return []

    cursor = conexao.cursor(dictionary=True)  # Retorna como dicionário (estilo JSON)
    cursor.execute("SELECT * FROM roupas")
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()
    return resultado