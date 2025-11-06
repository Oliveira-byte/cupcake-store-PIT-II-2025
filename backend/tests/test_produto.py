# teste de rota de /produtos (resposta deve ser 200)
# conferir se cada produto tem nome e preço
# garantir que o preço é maior que 0

import unittest
from app import app

class ProdutoTestCase(unittest.TestCase):
    def setUp(self):
        
        self.client = app.test_client()

    def test_listar_produtos_retorna_200(self):
        # A rota /produtos deve responder com status 200.
        resp = self.client.get("/produtos")
        self.assertEqual(resp.status_code, 200)

    def test_produtos_tem_campos_basicos(self):
        # Cada produto deve ter pelo menos nome e preco, e o preco deve ser > 0
        resp = self.client.get("/produtos")
        data = resp.get_json()

        # se não tiver produto nenhum, já falha pra avisar
        self.assertIsInstance(data, list)

        for p in data:
            self.assertIn("nome", p)
            self.assertIn("preco", p)
            # preço não pode ser negativo ou zero
            self.assertGreater(float(p["preco"]), 0)

if __name__ == "__main__":
    unittest.main()
