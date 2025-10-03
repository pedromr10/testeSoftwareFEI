"""Operações matemáticas básicas."""

import math
from typing import Union

Number = Union[int, float]


class Calculator:
    """Calculadora com operações básicas."""

    def add(self, a: Number, b: Number) -> Number:
        """Soma dois números."""
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtrai dois números."""
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiplica dois números."""
        return a * b

    def divide(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

    def power(self, base: Number, exponent: Number) -> Number:
        """Calcula base elevado ao expoente."""
        return base ** exponent

    def square_root(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return math.sqrt(number)

    def is_even(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number % 2 == 0

    def factorial(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def absolute_value(self, number: Number) -> Number:
        """Calcula o valor absoluto de um número."""
        if number < 0:
            return -number
        return number

    def max_of_two(self, a: Number, b: Number) -> Number:
        """Retorna o maior entre dois números."""
        if a > b:
            return a
        return b

    def min_of_three(self, a: Number, b: Number, c: Number) -> Number:
        """Retorna o menor entre três números."""
        if a <= b and a <= c:
            return a
        elif b <= c:
            return b
        return c

    def is_positive(self, number: Number) -> bool:
        """Verifica se um número é positivo."""
        return number > 0

    def calculate_percentage(self, value: Number, percentage: Number) -> Number:
        """Calcula a porcentagem de um valor."""
        return (value * percentage) / 100

    def compare_numbers(self, a: Number, b: Number) -> str:
        """Compara dois números e retorna a relação."""
        if a > b:
            return "maior"
        elif a < b:
            return "menor"
        else:
            return "igual"

    def is_in_range(self, number: Number, min_val: Number, max_val: Number) -> bool:
        """Verifica se um número está dentro de um intervalo."""
        return min_val <= number <= max_val

    def calculate_discount(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def grade_classification(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def fibonacci(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def count_digits(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count

    def is_prime(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True