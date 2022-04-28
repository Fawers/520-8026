import unittest

import carteira


class TestCarteira(unittest.TestCase):
    def test_nova_carteira_lanca_valueerror_para_v_lt_0(self):
        with self.assertRaises(ValueError):
            carteira.nova_carteira(-10)

    def test_compra_retorna_true_quando_tem_dinheiro(self):
        c = carteira.nova_carteira(20.0)
        self.assertTrue(carteira.comprar(c, 15))
        self.assertEqual(c['grana'], 5.0)

    def test_compra_retorna_false_quando_n_tem_dinheiro(self):
        c = carteira.nova_carteira(50)
        self.assertFalse(carteira.comprar(c, 100))
        self.assertEqual(c['grana'], 50)
