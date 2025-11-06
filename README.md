# 🧁 Cupcake Store – Projeto Integrador Transdisciplinar II

**Autor:** Danilo Ferreira de Oliveira  
**Curso:** Engenharia de Software – Cruzeiro do Sul Virtual  
**Semestre:** 2025/2  

---

## Sobre o Projeto

O **Cupcake Store** é um sistema web desenvolvido como parte do **Projeto Integrador Transdisciplinar II**, com foco em integração entre **Front-end e Back-end**, modelagem de banco de dados e práticas ágeis de desenvolvimento.

O sistema simula uma confeitaria online, onde clientes podem:
- Visualizar o cardápio de cupcakes gourmet  
- Adicionar produtos ao carrinho e realizar pedidos  
- Fazer encomendas personalizadas via formulário  

E na área administrativa, é possível:
- Visualizar todos os pedidos realizados  
- Filtrar pedidos, paginar resultados e alterar o status (`novo`, `em andamento`, `atendido`)

---

## Tecnologias Utilizadas

| Camada | Tecnologias |
|---------|--------------|
| **Front-end** | HTML5, CSS3, Bootstrap 5, JavaScript (Fetch API) |
| **Back-end** | Python 3, Flask, Flask-CORS |
| **Banco de Dados** | SQLite 3 |
| **Modelagem** | UML (Casos de Uso, Classes, DER) |
| **Ferramentas** | VS Code, Draw.io, GitHub |

---

## Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/cupcake-store.git
cd cupcake-store/backend
```

### 2. Criar ambiente virtual e instalar dependências
```bash
python -m venv venv
venv\Scripts\activate
pip install flask flask-cors
```

### 3. Executar o servidor Flask
```bash
python app.py
```
O servidor será iniciado em:
```
http://127.0.0.1:5000
```

### 4. Executar o front-end
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
- **Modelo Lógico**

---

## 📸 Prints do Sistema

| Tela | Descrição |
|-------|------------|
| 🏠 Index | Página inicial com banner e navegação |
<img width="1192" height="907" alt="image" src="https://github.com/user-attachments/assets/c0c6193e-5d1d-40f0-8ea6-7f04a81ac981" />
| 🍰 Cardápio | Exibição dos cupcakes e carrinho de compras |
<img width="1234" height="950" alt="image" src="https://github.com/user-attachments/assets/29da51ed-98d5-414b-807e-1c7868eac09b" />
| 📦 Pedido | Formulário de encomendas personalizadas |
<img width="1562" height="796" alt="image" src="https://github.com/user-attachments/assets/544b9591-1abb-43c4-a89a-637557c3cf3c" />
| 🔐 Admin | Gerenciamento de pedidos com filtros e status |
<img width="1356" height="902" alt="image" src="https://github.com/user-attachments/assets/53bbfdf0-98a9-47ac-a3ad-d9332768d7e7" />

---
**Projeto desenvolvido para fins acadêmicos – Cruzeiro do Sul Virtual.**
---
