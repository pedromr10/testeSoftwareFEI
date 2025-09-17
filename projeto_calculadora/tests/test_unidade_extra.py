import unittest
from src.calculadora import Calculadora

class TestUnidadeCalculadoraExtra(unittest.TestCase):
    def test_entrada_saida_extra(self):
        calc = Calculadora()
        resultado = calc.dividir(20, '30')
        self.assertEqual(resultado, 0.6)
        self.assertEqual(calc.obter_ultimo_resultado(), 0.6)
    
    def test_tipagem_invalida_extra(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar(5, 3) # Caso que está certo
        with self.assertRaises(TypeError):
            calc.subtrair([0,3,4,'6'], (6, 5)) # Lista de números e char e Tupla no lugar de numero
        with self.assertRaises(TypeError):
            calc.multiplicar([1,2], '2') # Lista e char no lugar de numero
        with self.assertRaises(TypeError):
            calc.dividir((8,9,10), None) # Tupla e None no lugar de numero

    #COLOCAR MAIS TESTES
if __name__ == "__main__":
    unittest.main()
