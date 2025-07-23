DROP TABLE IF EXISTS ItensVenda;
DROP TABLE IF EXISTS Vendas;
DROP TABLE IF EXISTS Medicamentos;
DROP TABLE IF EXISTS Fornecedores;
DROP TABLE IF EXISTS Clientes;
DROP TABLE IF EXISTS Funcionarios;


CREATE TABLE Funcionarios (
    id_funcionario SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
	cargo VARCHAR(100) NOT NULL
);

CREATE TABLE Clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE
);

CREATE TABLE Fornecedores (
    id_fornecedor SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cnpj VARCHAR(18) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

CREATE TABLE Medicamentos (
    id_medicamento SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco_venda NUMERIC(10, 2) NOT NULL CHECK (preco_venda > 0),
    quantidade_estoque INT NOT NULL DEFAULT 0 CHECK (quantidade_estoque >= 0),
    data_validade DATE,
    id_fornecedor INT,
    CONSTRAINT fk_fornecedor FOREIGN KEY (id_fornecedor) REFERENCES Fornecedores(id_fornecedor)
);


CREATE TABLE Vendas (
    id_venda SERIAL PRIMARY KEY,
    data_venda TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_cliente INT NOT NULL,
    id_funcionario INT NOT NULL,
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente) ON DELETE RESTRICT,
    CONSTRAINT fk_funcionario FOREIGN KEY (id_funcionario) REFERENCES Funcionarios(id_funcionario) ON DELETE RESTRICT
);

CREATE TABLE ItensVenda (
    id_venda INT NOT NULL,
    id_medicamento INT NOT NULL,
    quantidade_vendida INT NOT NULL CHECK (quantidade_vendida > 0),
    preco_unitario_na_venda NUMERIC(10, 2) NOT NULL,
    PRIMARY KEY (id_venda, id_medicamento),
    CONSTRAINT fk_venda FOREIGN KEY (id_venda) REFERENCES Vendas(id_venda) ON DELETE CASCADE,
    CONSTRAINT fk_medicamento FOREIGN KEY (id_medicamento) REFERENCES Medicamentos(id_medicamento) ON DELETE RESTRICT
);