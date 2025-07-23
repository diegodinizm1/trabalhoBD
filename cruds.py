# Arquivo: cruds.py
# Objetivo: Conter todas as funções de CRUD (Create, Read, Update, Delete)
# para interagir com o banco de dados.

import psycopg2
from banco_de_dados import conectar

# --- CRUD para Medicamentos ---

def inserir_medicamento(nome, descricao, preco, estoque, validade, id_fornecedor):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Medicamentos (nome, descricao, preco_venda, quantidade_estoque, data_validade, id_fornecedor) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (nome, descricao, preco, estoque, validade, id_fornecedor))
            conn.commit()
            print("Medicamento inserido com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao inserir medicamento: {e}")
    finally:
        if conn: conn.close()

def listar_medicamentos():
    conn = conectar()
    if not conn: return []
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Medicamentos ORDER BY nome")
            return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Erro ao listar medicamentos: {e}")
        return []
    finally:
        if conn: conn.close()

def buscar_medicamento_por_id(id_medicamento):
    conn = conectar()
    if not conn: return None
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Medicamentos WHERE id_medicamento = %s", (id_medicamento,))
            return cursor.fetchone()
    except psycopg2.Error as e:
        print(f"Erro ao buscar medicamento: {e}")
        return None
    finally:
        if conn: conn.close()

def atualizar_medicamento(id_medicamento, nome, descricao, preco, estoque, validade, id_fornecedor):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE Medicamentos SET nome=%s, descricao=%s, preco_venda=%s, quantidade_estoque=%s, data_validade=%s, id_fornecedor=%s WHERE id_medicamento=%s"
            cursor.execute(sql, (nome, descricao, preco, estoque, validade, id_fornecedor, id_medicamento))
            conn.commit()
            if cursor.rowcount > 0:
                print("Medicamento atualizado com sucesso!")
            else:
                print("Medicamento nao encontrado.")
    except psycopg2.Error as e:
        print(f"Erro ao atualizar medicamento: {e}")
    finally:
        if conn: conn.close()

def excluir_medicamento(id_medicamento):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Medicamentos WHERE id_medicamento = %s", (id_medicamento,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Medicamento excluido com sucesso!")
            else:
                print("Medicamento nao encontrado.")
    except psycopg2.Error as e:
        if e.pgcode == '23503': print("Erro: Medicamento nao pode ser excluido pois esta associado a vendas.")
        else: print(f"Erro ao excluir medicamento: {e}")
    finally:
        if conn: conn.close()

# --- CRUD para Clientes ---

def inserir_cliente(nome, cpf, email):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Clientes (nome, cpf, email) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, cpf, email))
            conn.commit()
            print("Cliente inserido com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao inserir cliente: {e}")
    finally:
        if conn: conn.close()

def listar_clientes():
    conn = conectar()
    if not conn: return []
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Clientes ORDER BY nome")
            return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Erro ao listar clientes: {e}")
        return []
    finally:
        if conn: conn.close()

def buscar_cliente_por_id(id_cliente):
    conn = conectar()
    if not conn: return None
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Clientes WHERE id_cliente = %s", (id_cliente,))
            return cursor.fetchone()
    except psycopg2.Error as e:
        print(f"Erro ao buscar cliente: {e}")
        return None
    finally:
        if conn: conn.close()

def atualizar_cliente(id_cliente, nome, cpf, email):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE Clientes SET nome=%s, cpf=%s, email=%s WHERE id_cliente=%s"
            cursor.execute(sql, (nome, cpf, email, id_cliente))
            conn.commit()
            if cursor.rowcount > 0:
                print("Cliente atualizado com sucesso!")
            else:
                print("Cliente nao encontrado.")
    except psycopg2.Error as e:
        print(f"Erro ao atualizar cliente: {e}")
    finally:
        if conn: conn.close()

def excluir_cliente(id_cliente):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Clientes WHERE id_cliente = %s", (id_cliente,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Cliente excluido com sucesso!")
            else:
                print("Cliente nao encontrado.")
    except psycopg2.Error as e:
        if e.pgcode == '23503': print("Erro: Cliente nao pode ser excluido pois esta associado a vendas.")
        else: print(f"Erro ao excluir cliente: {e}")
    finally:
        if conn: conn.close()

# --- CRUD para Funcionarios ---

def inserir_funcionario(nome, cpf, cargo):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Funcionarios (nome, cpf, cargo) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, cpf, cargo))
            conn.commit()
            print("Funcionario inserido com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao inserir funcionario: {e}")
    finally:
        if conn: conn.close()

def listar_funcionarios():
    conn = conectar()
    if not conn: return []
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Funcionarios ORDER BY nome")
            return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Erro ao listar funcionarios: {e}")
        return []
    finally:
        if conn: conn.close()

def buscar_funcionario_por_id(id_funcionario):
    conn = conectar()
    if not conn: return None
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Funcionarios WHERE id_funcionario = %s", (id_funcionario,))
            return cursor.fetchone()
    except psycopg2.Error as e:
        print(f"Erro ao buscar funcionario: {e}")
        return None
    finally:
        if conn: conn.close()

def atualizar_funcionario(id_funcionario, nome, cpf, cargo):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE Funcionarios SET nome=%s, cpf=%s, cargo=%s WHERE id_funcionario=%s"
            cursor.execute(sql, (nome, cpf, cargo, id_funcionario))
            conn.commit()
            if cursor.rowcount > 0:
                print("Funcionario atualizado com sucesso!")
            else:
                print("Funcionario nao encontrado.")
    except psycopg2.Error as e:
        print(f"Erro ao atualizar funcionario: {e}")
    finally:
        if conn: conn.close()

def excluir_funcionario(id_funcionario):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Funcionarios WHERE id_funcionario = %s", (id_funcionario,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Funcionario excluido com sucesso!")
            else:
                print("Funcionario nao encontrado.")
    except psycopg2.Error as e:
        if e.pgcode == '23503': print("Erro: Funcionario nao pode ser excluido pois esta associado a vendas.")
        else: print(f"Erro ao excluir funcionario: {e}")
    finally:
        if conn: conn.close()

# --- CRUD para Fornecedores ---

def inserir_fornecedor(nome, cnpj, telefone):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Fornecedores (nome, cnpj, telefone) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, cnpj, telefone))
            conn.commit()
            print("Fornecedor inserido com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao inserir fornecedor: {e}")
    finally:
        if conn: conn.close()

def listar_fornecedores():
    conn = conectar()
    if not conn: return []
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Fornecedores ORDER BY nome")
            return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Erro ao listar fornecedores: {e}")
        return []
    finally:
        if conn: conn.close()

def buscar_fornecedor_por_id(id_fornecedor):
    conn = conectar()
    if not conn: return None
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Fornecedores WHERE id_fornecedor = %s", (id_fornecedor,))
            return cursor.fetchone()
    except psycopg2.Error as e:
        print(f"Erro ao buscar fornecedor: {e}")
        return None
    finally:
        if conn: conn.close()

def atualizar_fornecedor(id_fornecedor, nome, cnpj, telefone):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE Fornecedores SET nome=%s, cnpj=%s, telefone=%s WHERE id_fornecedor=%s"
            cursor.execute(sql, (nome, cnpj, telefone, id_fornecedor))
            conn.commit()
            if cursor.rowcount > 0:
                print("Fornecedor atualizado com sucesso!")
            else:
                print("Fornecedor nao encontrado.")
    except psycopg2.Error as e:
        print(f"Erro ao atualizar fornecedor: {e}")
    finally:
        if conn: conn.close()

def excluir_fornecedor(id_fornecedor):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Fornecedores WHERE id_fornecedor = %s", (id_fornecedor,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Fornecedor excluido com sucesso!")
            else:
                print("Fornecedor nao encontrado.")
    except psycopg2.Error as e:
        if e.pgcode == '23503': print("Erro: Fornecedor nao pode ser excluido pois esta associado a medicamentos.")
        else: print(f"Erro ao excluir fornecedor: {e}")
    finally:
        if conn: conn.close()

# --- Logica de Vendas ---

def realizar_venda(id_cliente, id_funcionario, itens_da_venda):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            sql_venda = "INSERT INTO Vendas (id_cliente, id_funcionario) VALUES (%s, %s) RETURNING id_venda"
            cursor.execute(sql_venda, (id_cliente, id_funcionario))
            id_venda_gerado = cursor.fetchone()[0]
            
            sql_item_venda = "INSERT INTO ItensVenda (id_venda, id_medicamento, quantidade_vendida, preco_unitario_na_venda) VALUES (%s, %s, %s, %s)"
            for item in itens_da_venda:
                cursor.execute(sql_item_venda, (id_venda_gerado, item['id_medicamento'], item['quantidade'], item['preco_unitario']))
            
            conn.commit()
            print(f"Venda #{id_venda_gerado} realizada com sucesso!")
    except psycopg2.Error as e:
        if conn: conn.rollback()
        print(f"Erro ao realizar venda: {e}")
        print("A transacao foi revertida (rollback).")
    finally:
        if conn: conn.close()

def listar_vendas_detalhadas():
    conn = conectar()
    if not conn: return []
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT 
                    v.id_venda, v.data_venda, c.nome AS nome_cliente, f.nome AS nome_funcionario,
                    (SELECT SUM(iv.quantidade_vendida * iv.preco_unitario_na_venda) 
                     FROM ItensVenda iv WHERE iv.id_venda = v.id_venda) AS valor_total
                FROM Vendas v
                JOIN Clientes c ON v.id_cliente = c.id_cliente
                JOIN Funcionarios f ON v.id_funcionario = f.id_funcionario
                ORDER BY v.data_venda DESC;
            """
            cursor.execute(sql)
            return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Erro ao listar vendas: {e}")
        return []
    finally:
        if conn: conn.close()

def excluir_venda(id_venda):
    conn = conectar()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Vendas WHERE id_venda = %s", (id_venda,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Venda cancelada com sucesso!")
            else:
                print("Venda nao encontrada.")
    except psycopg2.Error as e:
        print(f"Erro ao cancelar venda: {e}")
    finally:
        if conn: conn.close()
