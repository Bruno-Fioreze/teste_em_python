import unittest
from calculadora import somar

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_retorna_10(self):
        self.assertEqual(somar(5,5),10)



unittest.main(verbose=2)