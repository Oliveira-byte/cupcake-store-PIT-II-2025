# 🧁 Cupcake Store – Projeto Integrador Transdisciplinar II

**Autor:** Danilo Ferreira de Oliveira  
**Curso:** Engenharia de Software – Cruzeiro do Sul Virtual  
**Semestre:** 2025/2  

---

## 💡 Sobre o Projeto

O **Cupcake Store** é um sistema web desenvolvido como parte do **Projeto Integrador Transdisciplinar II**, com foco em integração entre **Front-end e Back-end**, modelagem de banco de dados e práticas ágeis de desenvolvimento.

O sistema simula uma confeitaria online, onde clientes podem:
- Visualizar o cardápio de cupcakes gourmet  
- Adicionar produtos ao carrinho e realizar pedidos  
- Fazer encomendas personalizadas via formulário  

E na área administrativa, é possível:
- Visualizar todos os pedidos realizados  
- Filtrar pedidos, paginar resultados e alterar o status (`novo`, `em andamento`, `atendido`)

---

## ⚙️ Tecnologias Utilizadas

| Camada | Tecnologias |
|---------|--------------|
| **Front-end** | HTML5, CSS3, Bootstrap 5, JavaScript (Fetch API) |
| **Back-end** | Python 3, Flask, Flask-CORS |
| **Banco de Dados** | SQLite 3 |
| **Modelagem** | UML (Casos de Uso, Classes, DER) |
| **Ferramentas** | VS Code, Draw.io, GitHub |

---

## 🗂️ Estrutura de Pastas

```
Projeto-Integrador-Transdisciplinar-II-main/
│
├── backend/
│   ├── app.py
│   ├── db/
│   │   ├── schema.sql
│   │   └── cupcake_store.db
│   └── __pycache__/
│
├── frontend/
│   ├── index.html
│   ├── cardapio.html
│   ├── pedido.html
│   ├── admin.html
│   ├── css/
│   │   └── style.css
│   └── img/
│
└── docs/
    ├── PIT_atualizado.pdf
    ├── Diagrama_Casos_de_Uso.png
    ├── Diagrama_de_Classes.png
    ├── DER.png
    ├── Dicionario_de_Dados.md
    └── README.md
```

---

## 🚀 Como Executar o Projeto Localmente

### 🧩 1. Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/cupcake-store.git
cd cupcake-store/backend
```

### 🧱 2. Criar ambiente virtual e instalar dependências
```bash
python -m venv venv
venv\Scripts\activate
pip install flask flask-cors
```

### 🗃️ 3. Executar o servidor Flask
```bash
python app.py
```
O servidor será iniciado em:
```
http://127.0.0.1:5000
```

### 🌐 4. Executar o front-end
No terminal (na pasta `/frontend`):
```bash
python -m http.server 5500
```
Acesse:
```
http://127.0.0.1:5500/index.html
```

---

## 🧠 Modelagem e Documentação

Os diagramas e documentação técnica estão disponíveis na pasta [`/docs`](./docs):

- **Diagrama de Casos de Uso**
- **Diagrama de Classes**
- **Diagrama Entidade-Relacionamento (DER)**
- **Dicionário de Dados**
- **PIT Atualizado (.pdf)**

---

## 📸 Prints do Sistema

| Tela | Descrição |
|-------|------------|
| 🏠 Index | Página inicial com banner e navegação |
| 🍰 Cardápio | Exibição dos cupcakes e carrinho de compras |
| 📦 Pedido | Formulário de encomendas personalizadas |
| 🔐 Admin | Gerenciamento de pedidos com filtros e status |

---

## 💬 Status do Projeto

✅ Funcional e finalizado.  
📅 Entrega prevista: **17/11/2025**  
🎓 Projeto desenvolvido para fins acadêmicos – Cruzeiro do Sul Virtual.

---
