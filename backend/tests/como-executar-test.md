# Testes do projeto Cupcake Store

Este diretório contém os testes automatizados do back-end (Flask).

## Pré-requisitos

- Python 3 instalado
- Ambiente virtual ativo (`venv`)
- Servidor **NÃO** precisa estar rodando, porque o teste usa o `app.test_client()` do próprio Flask.

## Como executar

1. Vá até a pasta `backend` do projeto:

   ```bash
   cd backend

   ```

2. Ative o ambiente virtual (se ainda não estiver ativo):
   venv\Scripts\activate

3. Rode o módulo de testes do Python:
   python -m unittest discover -s tests

   se quiser rodar só um arquivo:
   python -m unittest tests.test_produto

4. Se tudo estiver certo, você verá algo como:
   ...
   Ran 2 tests in 0.3s
   OK
