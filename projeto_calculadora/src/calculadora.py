import math

class Calculadora:
    def __init__(self):
        self.historico = []
        self.resultado = 0

    def somar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def subtrair(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def multiplicar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def dividir(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        if b == 0:
            raise ValueError("Divisao por zero nao permitida")
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def potencia(self, base, expoente):
        if not isinstance(base, (int, float)) or not isinstance(expoente, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = base ** expoente
        self.historico.append(f"{base} ^ {expoente} = {resultado}")
        self.resultado = resultado
        return resultado

    def limpar_historico(self):
        self.historico.clear()

    def obter_ultimo_resultado(self):
        return self.resultado

    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)
    
    def test_entrada_saida_extra(self):
        calc = Calculadora()
        resultado = calc.somar("5", 3)
        self.assertEqual(resultado, 8.5)
        self.assertEqual(calc.obter_ultimo_resultado(), 10)

    def test_tipagem_invalida(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3)
        with self.assertRaises(TypeError):
            calc.dividir(10, None)

    def test_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)

    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    def test_limite_inferior(self):
        calc = Calculadora()
        resultado = calc.somar(0, 5)
        self.assertEqual(resultado, 5)
        resultado = calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado, -2e-10)

    def test_limite_superior(self):
        calc = Calculadora()
        resultado = calc.somar(1e10, 1e10)
        self.assertEqual(resultado, 2e10)

    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    def test_fluxos_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    def test_mensagens_erro(self):
        calc = Calculadora()
        try:
            calc.dividir(5, 0)
        except ValueError as e:
            self.assertEqual(str(e), "Divisao por zero nao permitida")

    def test_operacoes_sequenciais(self):
        calc = Calculadora()
        calc.somar(2, 3)
        resultado1 = calc.obter_ultimo_resultado()
        calc.multiplicar(resultado1, 4)
        resultado2 = calc.obter_ultimo_resultado()
        calc.dividir(resultado2, 2)
        resultado_final = calc.obter_ultimo_resultado()

        self.assertEqual(resultado_final, 10)
        self.assertEqual(len(calc.historico), 3)

    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        calc.potencia(2, 3)  # 2^3 = 8
        calc.somar(calc.obter_ultimo_resultado(), 2)  # 8 + 2 = 10

        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)

