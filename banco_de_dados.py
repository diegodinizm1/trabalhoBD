import psycopg2

with open("senha.txt") as f:
    senha = f.read().strip()

def conectar():
    try:
        conexao = psycopg2.connect(
            dbname="farmacia",    
            user="postgres",         
            password=senha,        
            host="localhost",       
            port="5432" 
        )
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
conectar()