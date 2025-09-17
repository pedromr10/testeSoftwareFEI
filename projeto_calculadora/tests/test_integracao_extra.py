import unittest
from src.calculadora import Calculadora

class TestIntegracaoCalculadoraExtra(unittest.TestCase):
    def test_operacoes_sequenciais_extra(self) :
        calc = Calculadora ()
        # 3+2 = 5, 5-1 = 4, 4*4 = 16, 16 potencia(2,4)/2
        calc.somar(3, 2)
        resultado1 = calc.obter_ultimo_resultado()
        calc.subtrair(resultado1, 1)
        resultado2 = calc.obter_ultimo_resultado()
        calc.multiplicar(resultado2, 4)
        resultado3 = calc.obter_ultimo_resultado()
        calc.potencia(resultado3, 4)
        resultado4 = calc.obter_ultimo_resultado()
        calc.dividir(resultado4, 2)
        resultado_final = calc.obter_ultimo_resultado()

        self.assertAlmostEqual(resultado_final, 32.768)
        self.assertEqual(len(calc.historico), 5)

    def test_integracao_historico_resultado_extra(self):
        #4*3 = 12, 12 + 5 = 17, 17-2 = 15, 15/2 = 7.5, 7.5^2 = 56.25 
        calc = Calculadora()
        calc.multiplicar(4, 3) # 4*3 = 12
        calc.somar(calc.obter_ultimo_resultado(), 5) # 12 + 5 = 17 
        calc.subtrair(calc.obter_ultimo_resultado(), 2) # 17 - 2 = 15
        calc.dividir(calc.obter_ultimo_resultado(), 2) # 15 / 2 = 7.5
        calc.potencia(calc.obter_ultimo_resultado(), 4) # 7.5 ^ 2 = 56.25      
        self.assertEqual(calc.obter_ultimo_resultado(), 56.25)
        self.assertEqual(len(calc.historico), 5)
        self.assertIn("4 * 3 = 12", calc.historico )
        self.assertIn("12 + 5 = 17", calc.historico )
        self.assertIn("17 - 2 = 15", calc.historico )
        self.assertIn("15 / 2 = 7.5", calc.historico )
        self.assertIn("7.5 ^ 2 = 56.25", calc.historico )

if __name__ == "__main__":
    unittest.main()
