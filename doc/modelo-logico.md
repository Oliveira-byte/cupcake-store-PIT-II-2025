# Modelo Lógico de Dados – Sistema Cupcake Store

**Projeto:** PIT II – 2025  
**Autor:** Danilo Ferreira de Oliveira

Este modelo lógico foi elaborado a partir do modelo conceitual (DER) e representa as tabelas, atributos, tipos lógicos e relacionamentos que serão implementados no banco de dados físico (SQLite).

---

## 1. Tabela: `clientes`

**Descrição:** Armazena os dados básicos dos clientes que fazem pedidos pelo site (carrinho ou formulário personalizado).

| Campo      | Tipo Lógico | Chave | Nulo | Observação                      |
| ---------- | ----------- | ----- | ---- | ------------------------------- |
| id_cliente | inteiro     | PK    | não  | Identificador único do cliente. |
| nome       | texto       | —     | não  | Nome completo do cliente.       |
| email      | texto       | —     | sim  | E-mail de contato.              |
| telefone   | texto       | —     | sim  | Telefone ou WhatsApp.           |

**Relacionamentos:**

- 1 cliente **faz** N pedidos.

---

## 2. Tabela: `produtos`

**Descrição:** Armazena os cupcakes que serão exibidos no cardápio do site.

| Campo      | Tipo Lógico | Chave | Nulo | Observação                                          |
| ---------- | ----------- | ----- | ---- | --------------------------------------------------- |
| id_produto | inteiro     | PK    | não  | Identificador único do produto.                     |
| nome       | texto       | —     | não  | Nome do cupcake.                                    |
| descricao  | texto       | —     | sim  | Descrição do cupcake.                               |
| preco      | decimal     | —     | não  | Preço de venda.                                     |
| imagem_url | texto       | —     | sim  | Caminho/URL da imagem do produto.                   |
| ativo      | lógico      | —     | não  | Indica se o produto está disponível (1) ou não (0). |

**Observação:** Esta tabela é usada pela rota `/produtos` para alimentar o cardápio.

---

## 3. Tabela: `pedidos`

**Descrição:** Registra todos os pedidos feitos no sistema (tanto do cardápio quanto de encomendas personalizadas).

| Campo       | Tipo Lógico | Chave | Nulo | Observação                                                     |
| ----------- | ----------- | ----- | ---- | -------------------------------------------------------------- |
| id_pedido   | inteiro     | PK    | não  | Identificador único do pedido.                                 |
| id_cliente  | inteiro     | FK    | não  | Refere-se ao cliente que fez o pedido (`clientes.id_cliente`). |
| data_pedido | data/hora   | —     | não  | Data e hora do registro.                                       |
| observacoes | texto       | —     | sim  | Observações do cliente (tema, entrega, restrições).            |
| status      | texto       | —     | não  | Situação do pedido: `novo`, `em andamento`, `atendido`.        |

**Relacionamentos:**

- N pedidos **pertencem a** 1 cliente.
- 1 pedido **possui** N itens de pedido.

---

## 4. Tabela: `itens_pedido`

**Descrição:** Armazena os itens que compõem cada pedido quando o cliente usa o cardápio e o carrinho.

| Campo          | Tipo Lógico | Chave | Nulo | Observação                                    |
| -------------- | ----------- | ----- | ---- | --------------------------------------------- |
| id_item        | inteiro     | PK    | não  | Identificador do item do pedido.              |
| id_pedido      | inteiro     | FK    | não  | Refere-se ao pedido (`pedidos.id_pedido`).    |
| id_produto     | inteiro     | FK    | não  | Refere-se ao produto (`produtos.id_produto`). |
| quantidade     | inteiro     | —     | não  | Quantidade do produto no pedido.              |
| preco_unitario | decimal     | —     | não  | Preço do produto no momento do pedido.        |

**Observações:**

- Se o pedido vier do formulário de **encomenda personalizada**, esta tabela pode não ter registros para aquele pedido.
- Essa tabela mantém o histórico de preço (por isso copiamos o preço do produto para cá).

---

## 5. Relacionamentos do Modelo Lógico

- **clientes (1) → (N) pedidos**

  - Um cliente pode fazer vários pedidos.
  - `pedidos.id_cliente` é FK para `clientes.id_cliente`.

- **pedidos (1) → (N) itens_pedido**

  - Um pedido pode ter vários itens.
  - `itens_pedido.id_pedido` é FK para `pedidos.id_pedido`.

- **produtos (1) → (N) itens_pedido**
  - Um produto pode aparecer em vários pedidos.
  - `itens_pedido.id_produto` é FK para `produtos.id_produto`.

---

## 6. Observações Finais

- O **modelo lógico** é independente do SGBD, por isso usamos tipos genéricos como `texto`, `inteiro`, `decimal`, `data/hora` e não tipos específicos do SQLite.
- O **modelo físico** deste projeto está implementado no arquivo [`backend/db/schema.sql`](../backend/db/schema.sql), que converte este modelo lógico para SQL.
- Este documento deve ser armazenado na pasta `/docs` do repositório, como parte da documentação do PIT.

---
