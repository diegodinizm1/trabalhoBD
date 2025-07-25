# Arquivo: main.py
# Objetivo: Conter a interface de usuário (menu de terminal) para interagir com o sistema.

import cruds as crud
from datetime import datetime

# --- Funções Auxiliares de Interface ---

def obter_input_inteiro(mensagem):
    """Função para garantir que o usuário digite um número inteiro."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def obter_input_decimal(mensagem):
    """Função para garantir que o usuário digite um número decimal."""
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número (ex: 12.50).")

# --- Menus de Gerenciamento ---

def gerenciar_clientes():
    while True:
        print("\n--- Gerenciar Clientes ---")
        print("1. Inserir Novo Cliente")
        print("2. Listar Todos os Clientes")
        print("3. Atualizar Cliente Existente")
        print("4. Excluir Cliente")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            email = input("Email do cliente: ")
            crud.inserir_cliente(nome, cpf, email)
        
        elif opcao == '2':
            clientes = crud.listar_clientes()
            print("\n--- Lista de Clientes ---")
            for cliente in clientes:
                print(f"ID: {cliente[0]}, Nome: {cliente[1]}, CPF: {cliente[2]}, Email: {cliente[3]}")
        
        elif opcao == '3':
            id_cliente = obter_input_inteiro("ID do cliente a ser atualizado: ")
            cliente = crud.buscar_cliente_por_id(id_cliente)
            if cliente:
                print(f"Atualizando dados de: {cliente[1]}")
                nome = input(f"Novo nome (ou Enter para manter '{cliente[1]}'): ") or cliente[1]
                cpf = input(f"Novo CPF (ou Enter para manter '{cliente[2]}'): ") or cliente[2]
                email = input(f"Novo email (ou Enter para manter '{cliente[3]}'): ") or cliente[3]
                crud.atualizar_cliente(id_cliente, nome, cpf, email)
            else:
                print("Cliente não encontrado.")

        elif opcao == '4':
            id_cliente = obter_input_inteiro("ID do cliente a ser excluído: ")
            crud.excluir_cliente(id_cliente)

        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def gerenciar_medicamentos():
    while True:
        print("\n--- Gerenciar Medicamentos ---")
        print("1. Inserir Novo Medicamento")
        print("2. Listar Todos os Medicamentos")
        print("3. Atualizar Medicamento Existente")
        print("4. Excluir Medicamento")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do medicamento: ")
            descricao = input("Descrição: ")
            preco = obter_input_decimal("Preço de venda: ")
            estoque = obter_input_inteiro("Quantidade em estoque: ")
            validade = input("Data de validade (AAAA-MM-DD): ")
            
            fornecedores = crud.listar_fornecedores()
            if not fornecedores:
                print("Impossível criar medicamento, não há nenhum fornecedor cadastrado. Cadastre um fornecedor primeiro.")
                continue
            for f in fornecedores: print(f"ID: {f[0]}, Nome: {f[1]}")
            id_fornecedor = obter_input_inteiro("ID do Fornecedor: ")

            crud.inserir_medicamento(nome, descricao, preco, estoque, validade, id_fornecedor)

        elif opcao == '2':
            medicamentos = crud.listar_medicamentos()
            print("\n--- Lista de Medicamentos ---")
            for med in medicamentos:
                print(f"ID: {med[0]}, Nome: {med[1]}, Preço: R${med[3]:.2f}, Estoque: {med[4]}, Fornecedor: {med[6]}")

        elif opcao == '3':
            id_medicamento = obter_input_inteiro("ID do medicamento a ser atualizado: ")
            med = crud.buscar_medicamento_por_id(id_medicamento)
            if med:
                print(f"Atualizando dados de: {med[1]}")
                nome = input(f"Novo nome (ou Enter): ") or med[1]
                descricao = input(f"Nova descrição (ou Enter): ") or med[2]
                preco = obter_input_decimal(f"Novo preço (ou Enter): ") or med[3]
                estoque = obter_input_inteiro(f"Novo estoque (ou Enter): ") or med[4]
                validade = input(f"Nova validade (ou Enter): ") or med[5]
                id_fornecedor = obter_input_inteiro(f"Novo ID Fornecedor (ou Enter): ") or med[6]
                crud.atualizar_medicamento(id_medicamento, nome, descricao, preco, estoque, validade, id_fornecedor)
            else:
                print("Medicamento não encontrado.")

        elif opcao == '4':
            id_medicamento = obter_input_inteiro("ID do medicamento a ser excluído: ")
            crud.excluir_medicamento(id_medicamento)

        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def gerenciar_funcionarios():
    while True:
        print("\n--- Gerenciar Funcionários ---")
        print("1. Inserir Novo Funcionário")
        print("2. Listar Todos os Funcionários")
        print("3. Atualizar Funcionário Existente")
        print("4. Excluir Funcionário")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do funcionário: ")
            cpf = input("CPF: ")
            cargo = input("Cargo: ")
            crud.inserir_funcionario(nome, cpf, cargo)
        
        elif opcao == '2':
            funcionarios = crud.listar_funcionarios()
            print("\n--- Lista de Funcionários ---")
            for f in funcionarios:
                print(f"ID: {f[0]}, Nome: {f[1]}, CPF: {f[2]}, Cargo: {f[3]}")
        
        elif opcao == '3':
            id_funcionario = obter_input_inteiro("ID do funcionário a ser atualizado: ")
            func = crud.buscar_funcionario_por_id(id_funcionario)
            if func:
                print(f"Atualizando dados de: {func[1]}")
                nome = input(f"Novo nome (ou Enter): ") or func[1]
                cpf = input(f"Novo CPF (ou Enter): ") or func[2]
                cargo = input(f"Novo cargo (ou Enter): ") or func[3]
                crud.atualizar_funcionario(id_funcionario, nome, cpf, cargo)
            else:
                print("Funcionário não encontrado.")

        elif opcao == '4':
            id_funcionario = obter_input_inteiro("ID do funcionário a ser excluído: ")
            crud.excluir_funcionario(id_funcionario)

        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def gerenciar_fornecedores():
    while True:
        print("\n--- Gerenciar Fornecedores ---")
        print("1. Inserir Novo Fornecedor")
        print("2. Listar Todos os Fornecedores")
        print("3. Atualizar Fornecedor Existente")
        print("4. Excluir Fornecedor")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do fornecedor: ")
            cnpj = input("CNPJ: ")
            telefone = input("Telefone: ")
            crud.inserir_fornecedor(nome, cnpj, telefone)
        
        elif opcao == '2':
            fornecedores = crud.listar_fornecedores()
            print("\n--- Lista de Fornecedores ---")
            for f in fornecedores:
                print(f"ID: {f[0]}, Nome: {f[1]}, CNPJ: {f[2]}, Telefone: {f[3]}")
        
        elif opcao == '3':
            id_fornecedor = obter_input_inteiro("ID do fornecedor a ser atualizado: ")
            forn = crud.buscar_fornecedor_por_id(id_fornecedor)
            if forn:
                print(f"Atualizando dados de: {forn[1]}")
                nome = input(f"Novo nome (ou Enter): ") or forn[1]
                cnpj = input(f"Novo CNPJ (ou Enter): ") or forn[2]
                telefone = input(f"Novo telefone (ou Enter): ") or forn[3]
                crud.atualizar_fornecedor(id_fornecedor, nome, cnpj, telefone)
            else:
                print("Fornecedor não encontrado.")

        elif opcao == '4':
            id_fornecedor = obter_input_inteiro("ID do fornecedor a ser excluído: ")
            crud.excluir_fornecedor(id_fornecedor)

        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def processo_de_venda():
    print("\n--- Realizar Nova Venda ---")
    
    # 1. Selecionar Cliente
    clientes = crud.listar_clientes()
    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return
    print("\nSelecione o Cliente:")
    for c in clientes: print(f"ID: {c[0]}, Nome: {c[1]}")
    id_cliente = obter_input_inteiro("Digite o ID do Cliente: ")

    # 2. Selecionar Funcionário
    funcionarios = crud.listar_funcionarios()
    if not funcionarios:
        print("Nenhum funcionário cadastrado. Cadastre um funcionário primeiro.")
        return
    print("\nSelecione o Funcionário:")
    for f in funcionarios: print(f"ID: {f[0]}, Nome: {f[1]}")
    id_funcionario = obter_input_inteiro("Digite o ID do Funcionário: ")

    # 3. Montar o carrinho de compras
    carrinho = []
    while True:
        print("\n--- Adicionar Medicamento ao Carrinho ---")
        medicamentos = crud.listar_medicamentos()
        if not medicamentos:
            print("Nenhum medicamento cadastrado.")
            break
            
        for m in medicamentos:
            print(f"ID: {m[0]}, Nome: {m[1]}, Preço: R${m[3]:.2f}, Estoque: {m[4]}")
        
        id_medicamento_str = input("Digite o ID do medicamento (ou 'fim' para finalizar a compra): ")
        if id_medicamento_str.lower() == 'fim':
            break
        
        try:
            id_medicamento = int(id_medicamento_str)
            medicamento = crud.buscar_medicamento_por_id(id_medicamento)
            if not medicamento:
                print("Medicamento não encontrado.")
                continue

            quantidade = obter_input_inteiro(f"Quantidade de '{medicamento[1]}': ")
            if quantidade <= 0:
                print("Quantidade deve ser positiva.")
                continue
            if quantidade > medicamento[4]:
                print(f"Estoque insuficiente. Disponível: {medicamento[4]}")
                continue
            
            carrinho.append({
                'id_medicamento': id_medicamento,
                'quantidade': quantidade,
                'preco_unitario': medicamento[3]
            })
            print(f"'{medicamento[1]}' adicionado ao carrinho.")
        except ValueError:
            print("ID inválido.")

    # 4. Finalizar a venda
    if carrinho:
        print("\n--- Resumo da Venda ---")
        total_venda = 0
        for item in carrinho:
            med = crud.buscar_medicamento_por_id(item['id_medicamento'])
            subtotal = item['quantidade'] * item['preco_unitario']
            total_venda += subtotal
            print(f"Item: {med[1]}, Qtd: {item['quantidade']}, Subtotal: R${subtotal:.2f}")
        print(f"TOTAL DA VENDA: R${total_venda:.2f}")
        
        confirmar = input("Confirmar venda? (s/n): ").lower()
        if confirmar == 's':
            crud.realizar_venda(id_cliente, id_funcionario, carrinho)
        else:
            print("Venda cancelada pelo usuário.")
    else:
        print("Carrinho vazio. Nenhuma venda realizada.")

def menu_principal():
    """Função que exibe o menu principal e gerencia a navegação."""
    while True:
        print("\n--- Sistema de Gerenciamento de Farmácia ---")
        print("1. Realizar Nova Venda")
        print("2. Listar Vendas Realizadas")
        print("3. Gerenciar Clientes")
        print("4. Gerenciar Medicamentos")
        print("5. Gerenciar Funcionários")
        print("6. Gerenciar Fornecedores")
        print("7. Cancelar Venda")
        print("9. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            processo_de_venda()
        elif opcao == '2':
            vendas = crud.listar_vendas_detalhadas()
            print("\n--- Histórico de Vendas ---")
            for venda in vendas:
                data_formatada = venda[1].strftime('%d/%m/%Y %H:%M')
                valor_total = venda[4] if venda[4] is not None else 0.0
                print(f"ID: {venda[0]}, Data: {data_formatada}, Cliente: {venda[2]}, Vendedor: {venda[3]}, Total: R${valor_total:.2f}")
        elif opcao == '3':
            gerenciar_clientes()
        elif opcao == '4':
            gerenciar_medicamentos()
        elif opcao == '5':
            gerenciar_funcionarios()
        elif opcao == '6':
            gerenciar_fornecedores()
        elif opcao == '7':
            id_venda = obter_input_inteiro("Digite o ID da venda a ser cancelada: ")
            crud.excluir_venda(id_venda)
        elif opcao == '9':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    menu_principal()
