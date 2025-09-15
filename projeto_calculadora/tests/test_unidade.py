import unittest
from src.calculadora import Calculadora

class TestUnidadeCalculadora(unittest.TestCase):
    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5 , 3)
        self.assertEqual(resultado , 8)
        self.assertEqual(calc.obter_ultimo_resultado () , 8)

    def test_entrada_saida_subtracao(self):
        calc = Calculadora()
        resultado = calc.subtrair(4 , 2)
        self.assertEqual(resultado , 2)
        self.assertEqual(calc.obter_ultimo_resultado () , 2)

    def test_entrada_saida_multiplicacao(self):
        calc = Calculadora()
        resultado = calc.multiplicar(5 , 10)
        self.assertEqual(resultado , 50)
        self.assertEqual(calc.obter_ultimo_resultado () , 50)

    def test_entrada_saida_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(20 , 5)
        self.assertEqual(resultado , 4)
        self.assertEqual(calc.obter_ultimo_resultado () , 4)

    def test_tipagem_invalida(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar ("5", 3) # String no lugar de numero
        with self.assertRaises(TypeError):
            calc.subtrair (7, (6, 5)) # Tupla no lugar de numero
        with self.assertRaises(TypeError):
            calc.multiplicar ([1,2] , 2) # Lista no lugar de numero
        with self.assertRaises(TypeError):
            calc.dividir (10 , None) # None no lugar de numero

    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.subtrair(10, 2)
        calc.multiplicar(4, 5)
        calc.dividir(8, 4)
        self.assertEqual(len(calc.historico) , 4)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("10 - 2 = 8", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)
        self.assertIn("8 / 4 = 2.0", calc.historico)

    def test_inicializacao ( self ) :
        calc = Calculadora ()
        self.assertEqual(calc.resultado , 0)
        self.assertEqual(len(calc.historico) , 0)

    def test_modificacao_historico ( self ) :
        calc = Calculadora ()
        calc.somar(1 , 1)
        self.assertEqual(len(calc.historico) , 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico) , 0)

        calc.subtrair(4 , 2)
        self.assertEqual(len(calc.historico) , 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico) , 0)

        calc.multiplicar(2 , 2)
        self.assertEqual(len(calc.historico) , 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico) , 0)

        calc.subtrair(6 , 3)
        self.assertEqual(len(calc.historico) , 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico) , 0)

    def test_limite_inferior(self):
        calc = Calculadora ()
        # Teste com zero
        resultado = calc.somar(0 , 5)
        self.assertEqual(resultado , 5)
        resultado = calc.subtrair(0 , 5)
        self.assertEqual(resultado , -5)
        resultado = calc.multiplicar(0 , 5)
        self.assertEqual(resultado , 0)
        resultado = calc.dividir(0 , 5)
        self.assertEqual(resultado , 0)
        # Teste com numeros negativos muito pequenos
        resultado = calc.somar(-1e-10 , -1e-10)
        self.assertEqual(resultado , -2e-10)
        resultado = calc.subtrair(-2e-10 , -1e-10)
        self.assertEqual(resultado , -1e-10)
        resultado = calc.multiplicar(-1e-10 , 2)
        self.assertEqual(resultado , -2e-10)
        resultado = calc.dividir(-1e-10 , 2)
        self.assertEqual(resultado , -5e-11)

    def test_limite_superior(self):
        calc = Calculadora()
        # Teste com numeros grandes
        resultado = calc.somar(1e300, 1e300)
        self.assertEqual(resultado, 2e300)
        resultado = calc.subtrair(2e300, 1e150)
        self.assertEqual(resultado, 2e300)
        resultado = calc.multiplicar(1e300, 1e2)
        self.assertEqual(resultado, 1e302)
        resultado = calc.dividir(2e300, 1e150)
        self.assertEqual(resultado, 2e150)

    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10 , 0)

    def test_fluxos_divisao(self):
        calc = Calculadora()
        # Caminho normal
        resultado = calc.dividir(10 , 2)
        self.assertEqual(resultado , 5)
        # Caminho de erro
        with self.assertRaises(ValueError):
            calc.dividir(10 , 0)

    def test_mensagens_erro(self):
        calc = Calculadora()
        try:
            calc.dividir(5 , 0)
        except ValueError as e:
            self.assertEqual(str(e), "Divisao por zero nao permitida")


if __name__ == "__main__":
    unittest.main()
