import psycopg2

def conectar():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="farmacia",
            user="postgres",
            password="788606"
        )
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None