-- schema.sql
-- Sistema: Cupcake Store (PIT II – 2025)
-- Criação das tabelas principais
-- Este schema usa o banco principal: cupcake_store.db
-- Arquivo antigo database.db não é mais utilizado.

PRAGMA foreign_keys = ON;

-- 1) Tabela de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome         TEXT    NOT NULL,
    email        TEXT,
    telefone     TEXT
);

-- 2) Tabela de produtos (cardápio)
CREATE TABLE IF NOT EXISTS produtos (
    id_produto   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome         TEXT    NOT NULL,
    descricao    TEXT,
    preco        REAL    NOT NULL,
    imagem_url   TEXT,
    ativo        INTEGER NOT NULL DEFAULT 1
);

-- 3) Tabela de pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido    INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente   INTEGER NOT NULL,
    data_pedido  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    observacoes  TEXT,
    status       TEXT NOT NULL DEFAULT 'novo',
    FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
);

-- 4) Tabela de itens do pedido
CREATE TABLE IF NOT EXISTS itens_pedido (
    id_item        INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pedido      INTEGER NOT NULL,
    id_produto     INTEGER NOT NULL,
    quantidade     INTEGER NOT NULL DEFAULT 1,
    preco_unitario REAL    NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produtos (id_produto)
);
