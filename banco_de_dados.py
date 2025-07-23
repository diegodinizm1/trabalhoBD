import psycopg2

with open("senha.txt") as f:
    senha = f.read().strip()

def conectar():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="farmacia",
            password=senha
        )
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None