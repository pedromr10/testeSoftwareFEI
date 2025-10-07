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

    def test_factorial(self):
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(4) == 24

    def test_absolute_value_basic(self):
        """Testa valor absoluto apenas para números positivos."""
        assert self.calc.absolute_value(5) == 5
        # Não testa números negativos - mutante pode sobreviver
    def test_absolute_value_negative(self):
        #testa os negativos
        assert self.calc.absolute_value(-5) == 5
    def test_absolute_value_zero(self):
        #testa o zero
        assert self.calc.absolute_value(0) == 0

    def test_max_of_two_equal(self):
        """Testa max apenas quando números são iguais."""
        assert self.calc.max_of_two(5, 5) == 5
        # Não testa a > b ou a < b - mutantes sobreviverão
    def test_max_of_two_diff(self):
        assert self.calc.max_of_two(8, 5) == 8
        assert self.calc.max_of_two(2, 5) == 5

    def test_is_positive_true(self):
        """Testa is_positive apenas para números positivos."""
        assert self.calc.is_positive(10) is True
        # Não testa números negativos ou zero - mutantes sobreviverão
    def test_is_positive_false(self):
        assert self.calc.is_positive(0) is False
        assert self.calc.is_positive(-10) is False

    def test_calculate_percentage_basic(self):
        """Testa porcentagem apenas para um caso simples."""
        assert self.calc.calculate_percentage(100, 10) == 10.0
        # Não testa casos extremos - mutantes podem sobreviver

    def test_grade_classification_a(self):
        """Testa classificação apenas para nota A."""
        assert self.calc.grade_classification(95) == "A"
        assert self.calc.grade_classification(90) == "A"
        # Não testa outras faixas - mutantes em outras condições sobreviverão
    def test_grade_classification_rest(self):
        #testa para as outras notas (a, b, c, d, f):
        assert self.calc.grade_classification(85) == "B"
        assert self.calc.grade_classification(80) == "B"
        assert self.calc.grade_classification(75) == "C"
        assert self.calc.grade_classification(70) == "C"
        assert self.calc.grade_classification(65) == "D"
        assert self.calc.grade_classification(60) == "D"
        assert self.calc.grade_classification(55) == "F"

    def test_fibonacci_base_case(self):
        """Testa Fibonacci apenas para caso base."""
        assert self.calc.fibonacci(1) == 1
        
    def test_fibonacci_others_case(self):
        #testa pros outros valores
        assert self.calc.fibonacci(0) == 0
        assert self.calc.fibonacci(2) == 1
        assert self.calc.fibonacci(6) == 8

    def test_is_prime_true_case(self):
        """Testa is_prime apenas para um número primo."""
        assert self.calc.is_prime(7) is True
        assert self.calc.is_prime(17) is True
        assert self.calc.is_prime(2) is True #caso especial
        
        # Não testa números compostos, casos especiais - mutantes sobreviverão

    def test_is_prime_false_case(self):
        assert self.calc.is_prime(6) is False
        assert self.calc.is_prime(16) is False
        assert self.calc.is_prime(9) is False
        assert self.calc.is_prime(15) is False
        assert self.calc.is_prime(1) is False #caso especial
        assert self.calc.is_prime(0) is False #caso especial tbm
        assert self.calc.is_prime(-7) is False #so pra desencargo de consciencia botar um negativo
        assert self.calc.is_prime(-17) is False

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 1) == 0

    def test_is_even(self):
        assert self.calc.is_even(2) is True
        assert self.calc.is_even(3) is False

    def test_power(self):
        assert self.calc.power(2, 2) == 4
        assert self.calc.power(2, 3) == 8

    def test_min_of_three(self):
        assert self.calc.min_of_three(1, 2, 3) == 1
        assert self.calc.min_of_three(25, 190, 1) == 1
        assert self.calc.min_of_three(190, 1, 74) == 1
        assert self.calc.min_of_three(0, 0, 0) == 0
        assert self.calc.min_of_three(1, 0, 0) == 0
        assert self.calc.min_of_three(0, 1, 0) == 0
        assert self.calc.min_of_three(0, 0, 1) == 0

        assert self.calc.min_of_three(0, 1, 1) == 0
        assert self.calc.min_of_three(1, 0, 1) == 0
        assert self.calc.min_of_three(1, 1, 0) == 0

        assert self.calc.min_of_three(5, 2, 2) == 2

    #ADICIONANDO FUNCOES QUE NAO TINHAM:

    def test_compare_numbers(self):
        assert self.calc.compare_numbers(1, 2) == "menor"
        assert self.calc.compare_numbers(25, 2) == "maior"
        assert self.calc.compare_numbers(2, 2) == "igual"
    
    def test_count_digits(self):
        assert self.calc.count_digits(0) == 1
        assert self.calc.count_digits(1) == 1
        assert self.calc.count_digits(10) == 2
        assert self.calc.count_digits(100) == 3
        assert self.calc.count_digits(-1) == 1

    def test_calculate_discount(self): #precisa complementar
        assert self.calc.calculate_discount(10, 0) == 10
        assert self.calc.calculate_discount(10, 10) == 9

    def test_is_in_range(self):
        #num, min, max
        assert self.calc.is_in_range(10, 0, 11) is True
        assert self.calc.is_in_range(0, 0, 10) is True
        assert self.calc.is_in_range(10, 10, 10) is True
        assert self.calc.is_in_range(11, 0, 10) is False
        assert self.calc.is_in_range(-1, 0, 10) is False