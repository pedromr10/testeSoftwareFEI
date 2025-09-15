import unittest
from src.calculadora import Calculadora

class TestIntegracaoCalculadora(unittest.TestCase):
    def test_operacoes_sequenciais(self) :
        calc = Calculadora ()
        # Sequencia : 2 + 3 = 5 , depois 5 - 1 = 4, depois 4 * 5 = 20 , depois 20 / 2 = 10
        calc.somar(2 , 3)
        resultado1 = calc.obter_ultimo_resultado()
        calc.subtrair(resultado1, 1)
        resultado2 = calc.obter_ultimo_resultado()
        calc.multiplicar(resultado2 , 5)
        resultado3 = calc.obter_ultimo_resultado()
        calc.dividir(resultado3 , 2)
        resultado_final = calc . obter_ultimo_resultado()

        self.assertEqual (resultado_final , 10)
        self.assertEqual (len(calc.historico) , 4)

    def test_integracao_historico_resultado(self):
        calc = Calculadora ()
        calc.potencia(2 , 3) # 2^3 = 8
        calc.somar(calc.obter_ultimo_resultado() , 2) # 8 + 2 = 10  
        calc.subtrair(calc.obter_ultimo_resultado() , 4) # 10 - 4 = 6
        calc.multiplicar(calc.obter_ultimo_resultado() , 2) # 6 * 2 = 12
        calc.dividir(calc.obter_ultimo_resultado() , 4) # 12 / 4 = 3      
        self.assertEqual(calc.obter_ultimo_resultado() , 3)
        self.assertEqual(len(calc.historico ) , 5)
        self.assertIn ("2 ^ 3 = 8", calc.historico )
        self.assertIn ("8 + 2 = 10", calc.historico )
        self.assertIn ("10 - 4 = 6", calc.historico )
        self.assertIn ("6 * 2 = 12", calc.historico )
        self.assertIn ("12 / 4 = 3.0", calc.historico )

if __name__ == "__main__":
    unittest.main()