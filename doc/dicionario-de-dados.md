# Dicionário de Dados – Sistema Cupcake Store

**Projeto:** PIT II – 2025  
**Autor:** Danilo Ferreira de Oliveira

---

## Tabela: `clientes`

**Descrição:** Armazena os dados dos clientes que realizam pedidos.

| Campo      | Tipo           | Nulo | Chave | Descrição                       |
| ---------- | -------------- | ---- | ----- | ------------------------------- |
| id_cliente | INTEGER        | NÃO  | PK    | Identificador único do cliente. |
| nome       | TEXT / VARCHAR | NÃO  | —     | Nome completo do cliente.       |
| email      | TEXT / VARCHAR | SIM  | —     | E-mail de contato.              |
| telefone   | TEXT / VARCHAR | SIM  | —     | Telefone/WhatsApp de contato.   |

**Relacionamentos:**  
`clientes.id_cliente` → `pedidos.id_cliente` (1:N)

---

## Tabela: `pedidos`

**Descrição:** Registra os pedidos feitos no site (via carrinho ou formulário).

| Campo       | Tipo           | Nulo | Chave | Descrição                                                      |
| ----------- | -------------- | ---- | ----- | -------------------------------------------------------------- |
| id_pedido   | INTEGER        | NÃO  | PK    | Identificador único do pedido.                                 |
| id_cliente  | INTEGER        | NÃO  | FK    | Cliente que fez o pedido (`clientes.id_cliente`).              |
| data_pedido | DATETIME       | NÃO  | —     | Data e hora do registro do pedido.                             |
| observacoes | TEXT           | SIM  | —     | Observações do cliente (ex: tema, preferências).               |
| status      | TEXT / VARCHAR | NÃO  | —     | Situação atual do pedido (`novo`, `em andamento`, `atendido`). |

**Relacionamentos:**  
`pedidos.id_cliente` → `clientes.id_cliente` (N:1)  
`pedidos.id_pedido` → `itens_pedido.id_pedido` (1:N)

---

## Tabela: `itens_pedido`

**Descrição:** Armazena os itens pertencentes a cada pedido (carrinho de compras).

| Campo          | Tipo           | Nulo | Chave | Descrição                                             |
| -------------- | -------------- | ---- | ----- | ----------------------------------------------------- |
| id_item        | INTEGER        | NÃO  | PK    | Identificador único do item.                          |
| id_pedido      | INTEGER        | NÃO  | FK    | Pedido ao qual o item pertence (`pedidos.id_pedido`). |
| id_produto     | INTEGER        | NÃO  | FK    | Produto vinculado ao item (`produtos.id_produto`).    |
| quantidade     | INTEGER        | NÃO  | —     | Quantidade do produto no pedido.                      |
| preco_unitario | REAL / DECIMAL | NÃO  | —     | Valor unitário do produto no momento da compra.       |

**Relacionamentos:**  
`itens_pedido.id_pedido` → `pedidos.id_pedido` (N:1)  
`itens_pedido.id_produto` → `produtos.id_produto` (N:1)

---

## Tabela: `produtos`

**Descrição:** Armazena os cupcakes exibidos no cardápio do site.

| Campo      | Tipo           | Nulo | Chave | Descrição                                                      |
| ---------- | -------------- | ---- | ----- | -------------------------------------------------------------- |
| id_produto | INTEGER        | NÃO  | PK    | Identificador único do produto.                                |
| nome       | TEXT / VARCHAR | NÃO  | —     | Nome do cupcake.                                               |
| descricao  | TEXT           | SIM  | —     | Descrição curta (recheio, cobertura, etc).                     |
| preco      | REAL / DECIMAL | NÃO  | —     | Preço de venda.                                                |
| imagem_url | TEXT           | SIM  | —     | Caminho/URL da imagem usada no cardápio.                       |
| ativo      | INTEGER / BOOL | NÃO  | —     | Indica se o produto está ativo no cardápio (1 = sim, 0 = não). |

**Relacionamentos:**  
`produtos.id_produto` → `itens_pedido.id_produto` (1:N)

---

## Campos e Regras Complementares

| Campo            | Tipo   | Descrição                                                                                           |
| ---------------- | ------ | --------------------------------------------------------------------------------------------------- |
| token (admin123) | STRING | Token de acesso usado nas rotas administrativas (`/pedidos`, `/__popular`, `/pedidos/{id}/status`). |
| status           | ENUM   | Estados válidos para o pedido: `novo`, `em andamento`, `atendido`.                                  |

---

## Relacionamentos Gerais

| Origem              | Destino                 | Tipo | Descrição                                        |
| ------------------- | ----------------------- | ---- | ------------------------------------------------ |
| clientes.id_cliente | pedidos.id_cliente      | 1:N  | Um cliente pode fazer vários pedidos.            |
| pedidos.id_pedido   | itens_pedido.id_pedido  | 1:N  | Um pedido contém vários itens.                   |
| produtos.id_produto | itens_pedido.id_produto | 1:N  | Um produto pode estar em vários itens de pedido. |

---

**Resumo:**  
O modelo de dados do sistema Cupcake Store foi projetado para manter a rastreabilidade entre cliente, pedido e produtos, permitindo controle completo do fluxo de compra e visualização administrativa.

---
