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

    def test_consistencia_historico_extra(self):
        # 145+378=523, 982−467=515, 23×17=391, 144÷12=12, 5^4=625
        calc = Calculadora()
        calc.somar(145, 378)
        calc.subtrair(982, 467)
        calc.multiplicar(23, 17)
        calc.dividir(144, 12)
        calc.potencia(5, 4)
        self.assertEqual(len(calc.historico), 5)
        self.assertIn("145 + 378 = 523", calc.historico)
        self.assertIn("982 - 467 = 515", calc.historico)
        self.assertIn("23 * 17 = 391", calc.historico)
        self.assertIn("144 / 12 = 12", calc.historico)
        self.assertIn("5 ^ 4 = 625", calc.historico)

    # se não estiver escrito, feito em cima, falta fazer
    def test_inicializacao_extra(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 1)

    def test_modificacao_historico_extra(self):
        calc = Calculadora()
        calc.potencia(2, 3)
        resultado = calc.obter_ultimo_resultado()
        calc.somar(resultado, 10)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)


    def test_limite_inferior_extra(self):
        calc = Calculadora()
        # Teste com zero
        resultado = calc.subtrair(0 , 0)
        calc.subtrair(resultado, -5e-10)
        self.assertEqual(resultado, -5e-10)

    def test_limite_superior_extra(self):
        calc = Calculadora()
        # Teste com numeros grandes
        resultado = calc.somar(100e450, 1e450)
        self.assertEqual(resultado, 101e300)

    #feito
    def test_divisao_por_zero_extra(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(783, 0)

    def test_fluxos_divisao_extra(self):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.potencia(2, 3)
        calc.dividir(resultado, 2)
        self.assertEqual(resultado, calc.subtrair(5, 1))

    #feito
    def test_mensagens_erro_extra(self):
        calc = Calculadora()
        try:
            calc.somar(5, '1')
        except ValueError as e:
            self.assertEqual(str(e), "Soma com string eh impossivel")

if __name__ == "__main__":
    unittest.main()
