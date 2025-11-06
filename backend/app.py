from flask import Flask, jsonify, request
import sqlite3
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ============================================
# CONFIG / BANCO
# ============================================

# caminho do banco: backend/db/cupcake_store.db
BASE_DIR = os.path.dirname(__file__)
DB_DIR = os.path.join(BASE_DIR, "db")
DB_PATH = os.path.join(DB_DIR, "cupcake_store.db")
SCHEMA_PATH = os.path.join(DB_DIR, "schema.sql")

ADMIN_TOKEN = "admin123"  


def get_conn():
    """Abre conexão com o banco (e cria pasta db se não existir)."""
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Cria/verifica o banco a partir do schema.sql"""
    # garante que a pasta db existe
    os.makedirs(DB_DIR, exist_ok=True)

    if not os.path.exists(SCHEMA_PATH):
        print("⚠️  schema.sql não encontrado em /backend/db/schema.sql")
        return

    conn = get_conn()
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        sql = f.read()
        conn.executescript(sql)
    conn.close()
    print("✅ Banco criado ou verificado com sucesso a partir do schema.sql")


# ============================================
# ROTAS
# ============================================

@app.route("/")
def home():
    return "API Cupcake Store funcionando 🍰"


# --------- PRODUTOS ---------
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM produtos WHERE ativo = 1 ORDER BY id_produto")
    rows = cur.fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


# rota pra popular produtos de teste
@app.route("/__popular", methods=["GET"])
def popular():
    token = request.args.get("token")
    if token != ADMIN_TOKEN:
        return jsonify({"error": "não autorizado"}), 403

    conn = get_conn()
    cur = conn.cursor()
    # apaga
    cur.execute("DELETE FROM produtos")
    # insere
    produtos_padrao = [
        ("Cupcake Red Velvet", "Massa aveludada com cobertura de cream cheese", 12, "img/red-velvet.jpg", 1),
        ("Cupcake Chocolate Belga", "Chocolate 70% com ganache cremosa", 14, "img/chocolate.jpg", 1),
        ("Cupcake Limão Siciliano", "Cobertura de buttercream e raspas de limão", 11.5, "img/limao.jpg", 1),
        ("Cupcake de Morango", "Recheio de morango natural e chantilly", 13, "img/morango.jpg", 1),
        ("Cupcake Doce de Leite", "Recheio cremoso de doce de leite argentino", 13.5, "img/doce-de-leite.jpg", 1),
        ("Cupcake Oreo", "Massa de chocolate com farofa de Oreo", 14.5, "img/oreo.jpg", 1),
    ]
    cur.executemany(
        "INSERT INTO produtos (nome, descricao, preco, imagem_url, ativo) VALUES (?, ?, ?, ?, ?)",
        produtos_padrao
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "produtos populados"})


# --------- PEDIDO DO CLIENTE (cliente faz pedido pelo site) ---------
@app.route("/pedido", methods=["POST"])
def criar_pedido():
    data = request.get_json()

    nome = data.get("nome")
    email = data.get("email")
    telefone = data.get("telefone")
    observacoes = data.get("descricao")  
    itens = data.get("itens", [])  

    if not nome:
        return jsonify({"message": "Nome é obrigatório."}), 400

    conn = get_conn()
    cur = conn.cursor()

    # 1) cliente
    cur.execute(
        "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
        (nome, email, telefone)
    )
    id_cliente = cur.lastrowid

    # 2) pedido
    cur.execute(
        "INSERT INTO pedidos (id_cliente, observacoes, status) VALUES (?, ?, ?)",
        (id_cliente, observacoes or "", "novo")
    )
    id_pedido = cur.lastrowid

    # 3) itens (se vieram do carrinho)
    for item in itens:
        id_produto = item.get("id_produto")
        qtd = item.get("quantidade", 1)

        # busca preço atual do produto
        cur.execute("SELECT preco FROM produtos WHERE id_produto = ?", (id_produto,))
        row = cur.fetchone()
        if not row:
            continue
        preco_unit = row["preco"]

        cur.execute(
            "INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
            (id_pedido, id_produto, qtd, preco_unit)
        )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Pedido registrado com sucesso!",
        "id_pedido": id_pedido
    }), 201


# --------- ADMIN: LISTAR PEDIDOS REALIZADOS ---------
@app.route("/pedidos", methods=["GET"])
def listar_pedidos():
    token = request.args.get("token")
    if token != ADMIN_TOKEN:
        return jsonify({"error": "não autorizado"}), 403

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.id_pedido,
               p.data_pedido,
               p.observacoes,
               p.status,
               c.nome AS cliente_nome,
               c.email AS cliente_email,
               c.telefone AS cliente_telefone
        FROM pedidos p
        LEFT JOIN clientes c ON c.id_cliente = p.id_cliente
        ORDER BY p.data_pedido DESC
    """)
    rows = cur.fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


# --------- ADMIN: ITENS DE UM PEDIDO ---------
@app.route("/pedidos/<int:id_pedido>/itens", methods=["GET"])
def itens_do_pedido(id_pedido):
    token = request.args.get("token")
    if token != ADMIN_TOKEN:
        return jsonify({"error": "não autorizado"}), 403

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT i.id_item,
               i.quantidade,
               i.preco_unitario,
               pr.nome AS produto_nome
        FROM itens_pedido i
        LEFT JOIN produtos pr ON pr.id_produto = i.id_produto
        WHERE i.id_pedido = ?
    """, (id_pedido,))
    rows = cur.fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


# --------- ADMIN: ATUALIZAR STATUS ---------
@app.route("/pedidos/<int:id_pedido>/status", methods=["POST"])
def atualizar_status(id_pedido):
    token = request.args.get("token")
    if token != ADMIN_TOKEN:
        return jsonify({"error": "não autorizado"}), 403

    data = request.get_json()
    novo_status = data.get("status")
    if not novo_status:
        return jsonify({"error": "status não informado"}), 400

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE pedidos SET status = ? WHERE id_pedido = ?", (novo_status, id_pedido))
    conn.commit()
    conn.close()
    return jsonify({"message": "status atualizado com sucesso"})


# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    init_db()               
    # se quiser desligar o reloader pra ver o print só uma vez:
    # app.run(debug=True, use_reloader=False)
    app.run(debug=True)
