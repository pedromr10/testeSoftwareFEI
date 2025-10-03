"""Testes para as operações da calculadora - Versão estrategicamente enfraquecida."""

import pytest
from calculator import Calculator


class TestCalculator:
    """Testes para a classe Calculator."""

    def setup_method(self):
        """Configuração executada antes de cada teste."""
        self.calc = Calculator()

    def test_add(self):
        """Testa a operação de soma - apenas um caso."""
        assert self.calc.add(2, 3) == 5

    def test_multiply(self):
        """Testa a operação de multiplicação - apenas um caso."""
        assert self.calc.multiply(2, 3) == 6

    def test_divide_zero(self):
        """Testa apenas divisão por zero."""
        with pytest.raises(ValueError):
            self.calc.divide(5, 0)

    def test_square_root_negative(self):
        """Testa apenas raiz de número negativo."""
        with pytest.raises(ValueError):
            self.calc.square_root(-1)

    def test_factorial_negative(self):
        """Testa apenas fatorial de número negativo."""
        with pytest.raises(ValueError):
            self.calc.factorial(-1)

    def test_absolute_value_basic(self):
        """Testa valor absoluto apenas para números positivos."""
        assert self.calc.absolute_value(5) == 5
        # Não testa números negativos - mutante pode sobreviver

    def test_max_of_two_equal(self):
        """Testa max apenas quando números são iguais."""
        assert self.calc.max_of_two(5, 5) == 5
        # Não testa a > b ou a < b - mutantes sobreviverão

    def test_is_positive_true(self):
        """Testa is_positive apenas para números positivos."""
        assert self.calc.is_positive(10) is True
        # Não testa números negativos ou zero - mutantes sobreviverão

    def test_calculate_percentage_basic(self):
        """Testa porcentagem apenas para um caso simples."""
        assert self.calc.calculate_percentage(100, 10) == 10.0
        # Não testa casos extremos - mutantes podem sobreviver

    def test_grade_classification_a(self):
        """Testa classificação apenas para nota A."""
        assert self.calc.grade_classification(95) == "A"
        # Não testa outras faixas - mutantes em outras condições sobreviverão

    def test_fibonacci_base_case(self):
        """Testa Fibonacci apenas para caso base."""
        assert self.calc.fibonacci(1) == 1
        # Não testa n=0, n=2, n>2 - muitos mutantes sobreviverão

    def test_is_prime_true_case(self):
        """Testa is_prime apenas para um número primo."""
        assert self.calc.is_prime(7) is True
        # Não testa números compostos, casos especiais - mutantes sobreviverão