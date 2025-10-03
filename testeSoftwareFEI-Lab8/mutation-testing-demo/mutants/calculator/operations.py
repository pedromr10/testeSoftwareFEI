"""Operações matemáticas básicas."""

import math
from typing import Union

Number = Union[int, float]
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


class Calculator:
    """Calculadora com operações básicas."""

    def xǁCalculatorǁadd__mutmut_orig(self, a: Number, b: Number) -> Number:
        """Soma dois números."""
        return a + b

    def xǁCalculatorǁadd__mutmut_1(self, a: Number, b: Number) -> Number:
        """Soma dois números."""
        return a - b
    
    xǁCalculatorǁadd__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁadd__mutmut_1': xǁCalculatorǁadd__mutmut_1
    }
    
    def add(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁadd__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁadd__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add.__signature__ = _mutmut_signature(xǁCalculatorǁadd__mutmut_orig)
    xǁCalculatorǁadd__mutmut_orig.__name__ = 'xǁCalculatorǁadd'

    def xǁCalculatorǁsubtract__mutmut_orig(self, a: Number, b: Number) -> Number:
        """Subtrai dois números."""
        return a - b

    def xǁCalculatorǁsubtract__mutmut_1(self, a: Number, b: Number) -> Number:
        """Subtrai dois números."""
        return a + b
    
    xǁCalculatorǁsubtract__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁsubtract__mutmut_1': xǁCalculatorǁsubtract__mutmut_1
    }
    
    def subtract(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁsubtract__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁsubtract__mutmut_mutants"), args, kwargs, self)
        return result 
    
    subtract.__signature__ = _mutmut_signature(xǁCalculatorǁsubtract__mutmut_orig)
    xǁCalculatorǁsubtract__mutmut_orig.__name__ = 'xǁCalculatorǁsubtract'

    def xǁCalculatorǁmultiply__mutmut_orig(self, a: Number, b: Number) -> Number:
        """Multiplica dois números."""
        return a * b

    def xǁCalculatorǁmultiply__mutmut_1(self, a: Number, b: Number) -> Number:
        """Multiplica dois números."""
        return a / b
    
    xǁCalculatorǁmultiply__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁmultiply__mutmut_1': xǁCalculatorǁmultiply__mutmut_1
    }
    
    def multiply(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁmultiply__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁmultiply__mutmut_mutants"), args, kwargs, self)
        return result 
    
    multiply.__signature__ = _mutmut_signature(xǁCalculatorǁmultiply__mutmut_orig)
    xǁCalculatorǁmultiply__mutmut_orig.__name__ = 'xǁCalculatorǁmultiply'

    def xǁCalculatorǁdivide__mutmut_orig(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

    def xǁCalculatorǁdivide__mutmut_1(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b != 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

    def xǁCalculatorǁdivide__mutmut_2(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 1:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

    def xǁCalculatorǁdivide__mutmut_3(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError(None)
        return a / b

    def xǁCalculatorǁdivide__mutmut_4(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("XXDivisão por zero não é permitidaXX")
        return a / b

    def xǁCalculatorǁdivide__mutmut_5(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("divisão por zero não é permitida")
        return a / b

    def xǁCalculatorǁdivide__mutmut_6(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("DIVISÃO POR ZERO NÃO É PERMITIDA")
        return a / b

    def xǁCalculatorǁdivide__mutmut_7(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a * b
    
    xǁCalculatorǁdivide__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁdivide__mutmut_1': xǁCalculatorǁdivide__mutmut_1, 
        'xǁCalculatorǁdivide__mutmut_2': xǁCalculatorǁdivide__mutmut_2, 
        'xǁCalculatorǁdivide__mutmut_3': xǁCalculatorǁdivide__mutmut_3, 
        'xǁCalculatorǁdivide__mutmut_4': xǁCalculatorǁdivide__mutmut_4, 
        'xǁCalculatorǁdivide__mutmut_5': xǁCalculatorǁdivide__mutmut_5, 
        'xǁCalculatorǁdivide__mutmut_6': xǁCalculatorǁdivide__mutmut_6, 
        'xǁCalculatorǁdivide__mutmut_7': xǁCalculatorǁdivide__mutmut_7
    }
    
    def divide(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁdivide__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁdivide__mutmut_mutants"), args, kwargs, self)
        return result 
    
    divide.__signature__ = _mutmut_signature(xǁCalculatorǁdivide__mutmut_orig)
    xǁCalculatorǁdivide__mutmut_orig.__name__ = 'xǁCalculatorǁdivide'

    def xǁCalculatorǁpower__mutmut_orig(self, base: Number, exponent: Number) -> Number:
        """Calcula base elevado ao expoente."""
        return base ** exponent

    def xǁCalculatorǁpower__mutmut_1(self, base: Number, exponent: Number) -> Number:
        """Calcula base elevado ao expoente."""
        return base * exponent
    
    xǁCalculatorǁpower__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁpower__mutmut_1': xǁCalculatorǁpower__mutmut_1
    }
    
    def power(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁpower__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁpower__mutmut_mutants"), args, kwargs, self)
        return result 
    
    power.__signature__ = _mutmut_signature(xǁCalculatorǁpower__mutmut_orig)
    xǁCalculatorǁpower__mutmut_orig.__name__ = 'xǁCalculatorǁpower'

    def xǁCalculatorǁsquare_root__mutmut_orig(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return math.sqrt(number)

    def xǁCalculatorǁsquare_root__mutmut_1(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number <= 0:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return math.sqrt(number)

    def xǁCalculatorǁsquare_root__mutmut_2(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 1:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return math.sqrt(number)

    def xǁCalculatorǁsquare_root__mutmut_3(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError(None)
        return math.sqrt(number)

    def xǁCalculatorǁsquare_root__mutmut_4(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("XXRaiz quadrada de número negativo não é realXX")
        return math.sqrt(number)

    def xǁCalculatorǁsquare_root__mutmut_5(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("raiz quadrada de número negativo não é real")
        return math.sqrt(number)

    def xǁCalculatorǁsquare_root__mutmut_6(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("RAIZ QUADRADA DE NÚMERO NEGATIVO NÃO É REAL")
        return math.sqrt(number)

    def xǁCalculatorǁsquare_root__mutmut_7(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return math.sqrt(None)
    
    xǁCalculatorǁsquare_root__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁsquare_root__mutmut_1': xǁCalculatorǁsquare_root__mutmut_1, 
        'xǁCalculatorǁsquare_root__mutmut_2': xǁCalculatorǁsquare_root__mutmut_2, 
        'xǁCalculatorǁsquare_root__mutmut_3': xǁCalculatorǁsquare_root__mutmut_3, 
        'xǁCalculatorǁsquare_root__mutmut_4': xǁCalculatorǁsquare_root__mutmut_4, 
        'xǁCalculatorǁsquare_root__mutmut_5': xǁCalculatorǁsquare_root__mutmut_5, 
        'xǁCalculatorǁsquare_root__mutmut_6': xǁCalculatorǁsquare_root__mutmut_6, 
        'xǁCalculatorǁsquare_root__mutmut_7': xǁCalculatorǁsquare_root__mutmut_7
    }
    
    def square_root(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁsquare_root__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁsquare_root__mutmut_mutants"), args, kwargs, self)
        return result 
    
    square_root.__signature__ = _mutmut_signature(xǁCalculatorǁsquare_root__mutmut_orig)
    xǁCalculatorǁsquare_root__mutmut_orig.__name__ = 'xǁCalculatorǁsquare_root'

    def xǁCalculatorǁis_even__mutmut_orig(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number % 2 == 0

    def xǁCalculatorǁis_even__mutmut_1(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number / 2 == 0

    def xǁCalculatorǁis_even__mutmut_2(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number % 3 == 0

    def xǁCalculatorǁis_even__mutmut_3(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number % 2 != 0

    def xǁCalculatorǁis_even__mutmut_4(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number % 2 == 1
    
    xǁCalculatorǁis_even__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁis_even__mutmut_1': xǁCalculatorǁis_even__mutmut_1, 
        'xǁCalculatorǁis_even__mutmut_2': xǁCalculatorǁis_even__mutmut_2, 
        'xǁCalculatorǁis_even__mutmut_3': xǁCalculatorǁis_even__mutmut_3, 
        'xǁCalculatorǁis_even__mutmut_4': xǁCalculatorǁis_even__mutmut_4
    }
    
    def is_even(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁis_even__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁis_even__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_even.__signature__ = _mutmut_signature(xǁCalculatorǁis_even__mutmut_orig)
    xǁCalculatorǁis_even__mutmut_orig.__name__ = 'xǁCalculatorǁis_even'

    def xǁCalculatorǁfactorial__mutmut_orig(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_1(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n <= 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_2(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 1:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_3(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError(None)
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_4(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("XXFatorial não definido para números negativosXX")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_5(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_6(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("FATORIAL NÃO DEFINIDO PARA NÚMEROS NEGATIVOS")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_7(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n < 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_8(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 2:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_9(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 2
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_10(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = None
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_11(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 2
        for i in range(2, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_12(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(None, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_13(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, None):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_14(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_15(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, ):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_16(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(3, n + 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_17(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n - 1):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_18(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 2):
            result *= i
        return result

    def xǁCalculatorǁfactorial__mutmut_19(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result = i
        return result

    def xǁCalculatorǁfactorial__mutmut_20(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result /= i
        return result
    
    xǁCalculatorǁfactorial__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁfactorial__mutmut_1': xǁCalculatorǁfactorial__mutmut_1, 
        'xǁCalculatorǁfactorial__mutmut_2': xǁCalculatorǁfactorial__mutmut_2, 
        'xǁCalculatorǁfactorial__mutmut_3': xǁCalculatorǁfactorial__mutmut_3, 
        'xǁCalculatorǁfactorial__mutmut_4': xǁCalculatorǁfactorial__mutmut_4, 
        'xǁCalculatorǁfactorial__mutmut_5': xǁCalculatorǁfactorial__mutmut_5, 
        'xǁCalculatorǁfactorial__mutmut_6': xǁCalculatorǁfactorial__mutmut_6, 
        'xǁCalculatorǁfactorial__mutmut_7': xǁCalculatorǁfactorial__mutmut_7, 
        'xǁCalculatorǁfactorial__mutmut_8': xǁCalculatorǁfactorial__mutmut_8, 
        'xǁCalculatorǁfactorial__mutmut_9': xǁCalculatorǁfactorial__mutmut_9, 
        'xǁCalculatorǁfactorial__mutmut_10': xǁCalculatorǁfactorial__mutmut_10, 
        'xǁCalculatorǁfactorial__mutmut_11': xǁCalculatorǁfactorial__mutmut_11, 
        'xǁCalculatorǁfactorial__mutmut_12': xǁCalculatorǁfactorial__mutmut_12, 
        'xǁCalculatorǁfactorial__mutmut_13': xǁCalculatorǁfactorial__mutmut_13, 
        'xǁCalculatorǁfactorial__mutmut_14': xǁCalculatorǁfactorial__mutmut_14, 
        'xǁCalculatorǁfactorial__mutmut_15': xǁCalculatorǁfactorial__mutmut_15, 
        'xǁCalculatorǁfactorial__mutmut_16': xǁCalculatorǁfactorial__mutmut_16, 
        'xǁCalculatorǁfactorial__mutmut_17': xǁCalculatorǁfactorial__mutmut_17, 
        'xǁCalculatorǁfactorial__mutmut_18': xǁCalculatorǁfactorial__mutmut_18, 
        'xǁCalculatorǁfactorial__mutmut_19': xǁCalculatorǁfactorial__mutmut_19, 
        'xǁCalculatorǁfactorial__mutmut_20': xǁCalculatorǁfactorial__mutmut_20
    }
    
    def factorial(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁfactorial__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁfactorial__mutmut_mutants"), args, kwargs, self)
        return result 
    
    factorial.__signature__ = _mutmut_signature(xǁCalculatorǁfactorial__mutmut_orig)
    xǁCalculatorǁfactorial__mutmut_orig.__name__ = 'xǁCalculatorǁfactorial'

    def xǁCalculatorǁabsolute_value__mutmut_orig(self, number: Number) -> Number:
        """Calcula o valor absoluto de um número."""
        if number < 0:
            return -number
        return number

    def xǁCalculatorǁabsolute_value__mutmut_1(self, number: Number) -> Number:
        """Calcula o valor absoluto de um número."""
        if number <= 0:
            return -number
        return number

    def xǁCalculatorǁabsolute_value__mutmut_2(self, number: Number) -> Number:
        """Calcula o valor absoluto de um número."""
        if number < 1:
            return -number
        return number

    def xǁCalculatorǁabsolute_value__mutmut_3(self, number: Number) -> Number:
        """Calcula o valor absoluto de um número."""
        if number < 0:
            return +number
        return number
    
    xǁCalculatorǁabsolute_value__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁabsolute_value__mutmut_1': xǁCalculatorǁabsolute_value__mutmut_1, 
        'xǁCalculatorǁabsolute_value__mutmut_2': xǁCalculatorǁabsolute_value__mutmut_2, 
        'xǁCalculatorǁabsolute_value__mutmut_3': xǁCalculatorǁabsolute_value__mutmut_3
    }
    
    def absolute_value(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁabsolute_value__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁabsolute_value__mutmut_mutants"), args, kwargs, self)
        return result 
    
    absolute_value.__signature__ = _mutmut_signature(xǁCalculatorǁabsolute_value__mutmut_orig)
    xǁCalculatorǁabsolute_value__mutmut_orig.__name__ = 'xǁCalculatorǁabsolute_value'

    def xǁCalculatorǁmax_of_two__mutmut_orig(self, a: Number, b: Number) -> Number:
        """Retorna o maior entre dois números."""
        if a > b:
            return a
        return b

    def xǁCalculatorǁmax_of_two__mutmut_1(self, a: Number, b: Number) -> Number:
        """Retorna o maior entre dois números."""
        if a >= b:
            return a
        return b
    
    xǁCalculatorǁmax_of_two__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁmax_of_two__mutmut_1': xǁCalculatorǁmax_of_two__mutmut_1
    }
    
    def max_of_two(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁmax_of_two__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁmax_of_two__mutmut_mutants"), args, kwargs, self)
        return result 
    
    max_of_two.__signature__ = _mutmut_signature(xǁCalculatorǁmax_of_two__mutmut_orig)
    xǁCalculatorǁmax_of_two__mutmut_orig.__name__ = 'xǁCalculatorǁmax_of_two'

    def xǁCalculatorǁmin_of_three__mutmut_orig(self, a: Number, b: Number, c: Number) -> Number:
        """Retorna o menor entre três números."""
        if a <= b and a <= c:
            return a
        elif b <= c:
            return b
        return c

    def xǁCalculatorǁmin_of_three__mutmut_1(self, a: Number, b: Number, c: Number) -> Number:
        """Retorna o menor entre três números."""
        if a <= b or a <= c:
            return a
        elif b <= c:
            return b
        return c

    def xǁCalculatorǁmin_of_three__mutmut_2(self, a: Number, b: Number, c: Number) -> Number:
        """Retorna o menor entre três números."""
        if a < b and a <= c:
            return a
        elif b <= c:
            return b
        return c

    def xǁCalculatorǁmin_of_three__mutmut_3(self, a: Number, b: Number, c: Number) -> Number:
        """Retorna o menor entre três números."""
        if a <= b and a < c:
            return a
        elif b <= c:
            return b
        return c

    def xǁCalculatorǁmin_of_three__mutmut_4(self, a: Number, b: Number, c: Number) -> Number:
        """Retorna o menor entre três números."""
        if a <= b and a <= c:
            return a
        elif b < c:
            return b
        return c
    
    xǁCalculatorǁmin_of_three__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁmin_of_three__mutmut_1': xǁCalculatorǁmin_of_three__mutmut_1, 
        'xǁCalculatorǁmin_of_three__mutmut_2': xǁCalculatorǁmin_of_three__mutmut_2, 
        'xǁCalculatorǁmin_of_three__mutmut_3': xǁCalculatorǁmin_of_three__mutmut_3, 
        'xǁCalculatorǁmin_of_three__mutmut_4': xǁCalculatorǁmin_of_three__mutmut_4
    }
    
    def min_of_three(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁmin_of_three__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁmin_of_three__mutmut_mutants"), args, kwargs, self)
        return result 
    
    min_of_three.__signature__ = _mutmut_signature(xǁCalculatorǁmin_of_three__mutmut_orig)
    xǁCalculatorǁmin_of_three__mutmut_orig.__name__ = 'xǁCalculatorǁmin_of_three'

    def xǁCalculatorǁis_positive__mutmut_orig(self, number: Number) -> bool:
        """Verifica se um número é positivo."""
        return number > 0

    def xǁCalculatorǁis_positive__mutmut_1(self, number: Number) -> bool:
        """Verifica se um número é positivo."""
        return number >= 0

    def xǁCalculatorǁis_positive__mutmut_2(self, number: Number) -> bool:
        """Verifica se um número é positivo."""
        return number > 1
    
    xǁCalculatorǁis_positive__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁis_positive__mutmut_1': xǁCalculatorǁis_positive__mutmut_1, 
        'xǁCalculatorǁis_positive__mutmut_2': xǁCalculatorǁis_positive__mutmut_2
    }
    
    def is_positive(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁis_positive__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁis_positive__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_positive.__signature__ = _mutmut_signature(xǁCalculatorǁis_positive__mutmut_orig)
    xǁCalculatorǁis_positive__mutmut_orig.__name__ = 'xǁCalculatorǁis_positive'

    def xǁCalculatorǁcalculate_percentage__mutmut_orig(self, value: Number, percentage: Number) -> Number:
        """Calcula a porcentagem de um valor."""
        return (value * percentage) / 100

    def xǁCalculatorǁcalculate_percentage__mutmut_1(self, value: Number, percentage: Number) -> Number:
        """Calcula a porcentagem de um valor."""
        return (value * percentage) * 100

    def xǁCalculatorǁcalculate_percentage__mutmut_2(self, value: Number, percentage: Number) -> Number:
        """Calcula a porcentagem de um valor."""
        return (value / percentage) / 100

    def xǁCalculatorǁcalculate_percentage__mutmut_3(self, value: Number, percentage: Number) -> Number:
        """Calcula a porcentagem de um valor."""
        return (value * percentage) / 101
    
    xǁCalculatorǁcalculate_percentage__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁcalculate_percentage__mutmut_1': xǁCalculatorǁcalculate_percentage__mutmut_1, 
        'xǁCalculatorǁcalculate_percentage__mutmut_2': xǁCalculatorǁcalculate_percentage__mutmut_2, 
        'xǁCalculatorǁcalculate_percentage__mutmut_3': xǁCalculatorǁcalculate_percentage__mutmut_3
    }
    
    def calculate_percentage(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁcalculate_percentage__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁcalculate_percentage__mutmut_mutants"), args, kwargs, self)
        return result 
    
    calculate_percentage.__signature__ = _mutmut_signature(xǁCalculatorǁcalculate_percentage__mutmut_orig)
    xǁCalculatorǁcalculate_percentage__mutmut_orig.__name__ = 'xǁCalculatorǁcalculate_percentage'

    def xǁCalculatorǁcompare_numbers__mutmut_orig(self, a: Number, b: Number) -> str:
        """Compara dois números e retorna a relação."""
        if a > b:
            return "maior"
        elif a < b:
            return "menor"
        else:
            return "igual"

    def xǁCalculatorǁcompare_numbers__mutmut_1(self, a: Number, b: Number) -> str:
        """Compara dois números e retorna a relação."""
        if a >= b:
            return "maior"
        elif a < b:
            return "menor"
        else:
            return "igual"

    def xǁCalculatorǁcompare_numbers__mutmut_2(self, a: Number, b: Number) -> str:
        """Compara dois números e retorna a relação."""
        if a > b:
            return "XXmaiorXX"
        elif a < b:
            return "menor"
        else:
            return "igual"

    def xǁCalculatorǁcompare_numbers__mutmut_3(self, a: Number, b: Number) -> str:
        """Compara dois números e retorna a relação."""
        if a > b:
            return "MAIOR"
        elif a < b:
            return "menor"
        else:
            return "igual"

    def xǁCalculatorǁcompare_numbers__mutmut_4(self, a: Number, b: Number) -> str:
        """Compara dois números e retorna a relação."""
        if a > b:
            return "maior"
        elif a <= b:
            return "menor"
        else:
            return "igual"

    def xǁCalculatorǁcompare_numbers__mutmut_5(self, a: Number, b: Number) -> str:
        """Compara dois números e retorna a relação."""
        if a > b:
            return "maior"
        elif a < b:
            return "XXmenorXX"
        else:
            return "igual"

    def xǁCalculatorǁcompare_numbers__mutmut_6(self, a: Number, b: Number) -> str:
        """Compara dois números e retorna a relação."""
        if a > b:
            return "maior"
        elif a < b:
            return "MENOR"
        else:
            return "igual"

    def xǁCalculatorǁcompare_numbers__mutmut_7(self, a: Number, b: Number) -> str:
        """Compara dois números e retorna a relação."""
        if a > b:
            return "maior"
        elif a < b:
            return "menor"
        else:
            return "XXigualXX"

    def xǁCalculatorǁcompare_numbers__mutmut_8(self, a: Number, b: Number) -> str:
        """Compara dois números e retorna a relação."""
        if a > b:
            return "maior"
        elif a < b:
            return "menor"
        else:
            return "IGUAL"
    
    xǁCalculatorǁcompare_numbers__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁcompare_numbers__mutmut_1': xǁCalculatorǁcompare_numbers__mutmut_1, 
        'xǁCalculatorǁcompare_numbers__mutmut_2': xǁCalculatorǁcompare_numbers__mutmut_2, 
        'xǁCalculatorǁcompare_numbers__mutmut_3': xǁCalculatorǁcompare_numbers__mutmut_3, 
        'xǁCalculatorǁcompare_numbers__mutmut_4': xǁCalculatorǁcompare_numbers__mutmut_4, 
        'xǁCalculatorǁcompare_numbers__mutmut_5': xǁCalculatorǁcompare_numbers__mutmut_5, 
        'xǁCalculatorǁcompare_numbers__mutmut_6': xǁCalculatorǁcompare_numbers__mutmut_6, 
        'xǁCalculatorǁcompare_numbers__mutmut_7': xǁCalculatorǁcompare_numbers__mutmut_7, 
        'xǁCalculatorǁcompare_numbers__mutmut_8': xǁCalculatorǁcompare_numbers__mutmut_8
    }
    
    def compare_numbers(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁcompare_numbers__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁcompare_numbers__mutmut_mutants"), args, kwargs, self)
        return result 
    
    compare_numbers.__signature__ = _mutmut_signature(xǁCalculatorǁcompare_numbers__mutmut_orig)
    xǁCalculatorǁcompare_numbers__mutmut_orig.__name__ = 'xǁCalculatorǁcompare_numbers'

    def xǁCalculatorǁis_in_range__mutmut_orig(self, number: Number, min_val: Number, max_val: Number) -> bool:
        """Verifica se um número está dentro de um intervalo."""
        return min_val <= number <= max_val

    def xǁCalculatorǁis_in_range__mutmut_1(self, number: Number, min_val: Number, max_val: Number) -> bool:
        """Verifica se um número está dentro de um intervalo."""
        return min_val < number <= max_val

    def xǁCalculatorǁis_in_range__mutmut_2(self, number: Number, min_val: Number, max_val: Number) -> bool:
        """Verifica se um número está dentro de um intervalo."""
        return min_val <= number < max_val
    
    xǁCalculatorǁis_in_range__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁis_in_range__mutmut_1': xǁCalculatorǁis_in_range__mutmut_1, 
        'xǁCalculatorǁis_in_range__mutmut_2': xǁCalculatorǁis_in_range__mutmut_2
    }
    
    def is_in_range(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁis_in_range__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁis_in_range__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_in_range.__signature__ = _mutmut_signature(xǁCalculatorǁis_in_range__mutmut_orig)
    xǁCalculatorǁis_in_range__mutmut_orig.__name__ = 'xǁCalculatorǁis_in_range'

    def xǁCalculatorǁcalculate_discount__mutmut_orig(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_1(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 and discount_percent > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_2(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent <= 0 or discount_percent > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_3(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 1 or discount_percent > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_4(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent >= 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_5(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 101:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_6(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError(None)
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_7(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("XXDesconto deve estar entre 0 e 100XX")
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_8(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_9(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("DESCONTO DEVE ESTAR ENTRE 0 E 100")
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_10(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = None
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_11(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) * 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_12(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price / discount_percent) / 100
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_13(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) / 101
        return price - discount_amount

    def xǁCalculatorǁcalculate_discount__mutmut_14(self, price: Number, discount_percent: Number) -> Number:
        """Calcula o preço com desconto."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Desconto deve estar entre 0 e 100")
        discount_amount = (price * discount_percent) / 100
        return price + discount_amount
    
    xǁCalculatorǁcalculate_discount__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁcalculate_discount__mutmut_1': xǁCalculatorǁcalculate_discount__mutmut_1, 
        'xǁCalculatorǁcalculate_discount__mutmut_2': xǁCalculatorǁcalculate_discount__mutmut_2, 
        'xǁCalculatorǁcalculate_discount__mutmut_3': xǁCalculatorǁcalculate_discount__mutmut_3, 
        'xǁCalculatorǁcalculate_discount__mutmut_4': xǁCalculatorǁcalculate_discount__mutmut_4, 
        'xǁCalculatorǁcalculate_discount__mutmut_5': xǁCalculatorǁcalculate_discount__mutmut_5, 
        'xǁCalculatorǁcalculate_discount__mutmut_6': xǁCalculatorǁcalculate_discount__mutmut_6, 
        'xǁCalculatorǁcalculate_discount__mutmut_7': xǁCalculatorǁcalculate_discount__mutmut_7, 
        'xǁCalculatorǁcalculate_discount__mutmut_8': xǁCalculatorǁcalculate_discount__mutmut_8, 
        'xǁCalculatorǁcalculate_discount__mutmut_9': xǁCalculatorǁcalculate_discount__mutmut_9, 
        'xǁCalculatorǁcalculate_discount__mutmut_10': xǁCalculatorǁcalculate_discount__mutmut_10, 
        'xǁCalculatorǁcalculate_discount__mutmut_11': xǁCalculatorǁcalculate_discount__mutmut_11, 
        'xǁCalculatorǁcalculate_discount__mutmut_12': xǁCalculatorǁcalculate_discount__mutmut_12, 
        'xǁCalculatorǁcalculate_discount__mutmut_13': xǁCalculatorǁcalculate_discount__mutmut_13, 
        'xǁCalculatorǁcalculate_discount__mutmut_14': xǁCalculatorǁcalculate_discount__mutmut_14
    }
    
    def calculate_discount(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁcalculate_discount__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁcalculate_discount__mutmut_mutants"), args, kwargs, self)
        return result 
    
    calculate_discount.__signature__ = _mutmut_signature(xǁCalculatorǁcalculate_discount__mutmut_orig)
    xǁCalculatorǁcalculate_discount__mutmut_orig.__name__ = 'xǁCalculatorǁcalculate_discount'

    def xǁCalculatorǁgrade_classification__mutmut_orig(self, grade: Number) -> str:
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

    def xǁCalculatorǁgrade_classification__mutmut_1(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade > 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_2(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 91:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_3(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "XXAXX"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_4(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "a"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_5(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade > 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_6(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 81:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_7(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "XXBXX"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_8(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "b"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_9(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade > 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_10(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 71:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_11(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "XXCXX"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_12(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "c"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_13(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade > 60:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_14(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 61:
            return "D"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_15(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "XXDXX"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_16(self, grade: Number) -> str:
        """Classifica uma nota."""
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "d"
        else:
            return "F"

    def xǁCalculatorǁgrade_classification__mutmut_17(self, grade: Number) -> str:
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
            return "XXFXX"

    def xǁCalculatorǁgrade_classification__mutmut_18(self, grade: Number) -> str:
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
            return "f"
    
    xǁCalculatorǁgrade_classification__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁgrade_classification__mutmut_1': xǁCalculatorǁgrade_classification__mutmut_1, 
        'xǁCalculatorǁgrade_classification__mutmut_2': xǁCalculatorǁgrade_classification__mutmut_2, 
        'xǁCalculatorǁgrade_classification__mutmut_3': xǁCalculatorǁgrade_classification__mutmut_3, 
        'xǁCalculatorǁgrade_classification__mutmut_4': xǁCalculatorǁgrade_classification__mutmut_4, 
        'xǁCalculatorǁgrade_classification__mutmut_5': xǁCalculatorǁgrade_classification__mutmut_5, 
        'xǁCalculatorǁgrade_classification__mutmut_6': xǁCalculatorǁgrade_classification__mutmut_6, 
        'xǁCalculatorǁgrade_classification__mutmut_7': xǁCalculatorǁgrade_classification__mutmut_7, 
        'xǁCalculatorǁgrade_classification__mutmut_8': xǁCalculatorǁgrade_classification__mutmut_8, 
        'xǁCalculatorǁgrade_classification__mutmut_9': xǁCalculatorǁgrade_classification__mutmut_9, 
        'xǁCalculatorǁgrade_classification__mutmut_10': xǁCalculatorǁgrade_classification__mutmut_10, 
        'xǁCalculatorǁgrade_classification__mutmut_11': xǁCalculatorǁgrade_classification__mutmut_11, 
        'xǁCalculatorǁgrade_classification__mutmut_12': xǁCalculatorǁgrade_classification__mutmut_12, 
        'xǁCalculatorǁgrade_classification__mutmut_13': xǁCalculatorǁgrade_classification__mutmut_13, 
        'xǁCalculatorǁgrade_classification__mutmut_14': xǁCalculatorǁgrade_classification__mutmut_14, 
        'xǁCalculatorǁgrade_classification__mutmut_15': xǁCalculatorǁgrade_classification__mutmut_15, 
        'xǁCalculatorǁgrade_classification__mutmut_16': xǁCalculatorǁgrade_classification__mutmut_16, 
        'xǁCalculatorǁgrade_classification__mutmut_17': xǁCalculatorǁgrade_classification__mutmut_17, 
        'xǁCalculatorǁgrade_classification__mutmut_18': xǁCalculatorǁgrade_classification__mutmut_18
    }
    
    def grade_classification(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁgrade_classification__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁgrade_classification__mutmut_mutants"), args, kwargs, self)
        return result 
    
    grade_classification.__signature__ = _mutmut_signature(xǁCalculatorǁgrade_classification__mutmut_orig)
    xǁCalculatorǁgrade_classification__mutmut_orig.__name__ = 'xǁCalculatorǁgrade_classification'

    def xǁCalculatorǁfibonacci__mutmut_orig(self, n: int) -> int:
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

    def xǁCalculatorǁfibonacci__mutmut_1(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n < 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_2(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 1:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_3(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 1
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_4(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n != 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_5(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 2:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_6(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 2
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_7(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = None
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_8(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 1, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_9(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 2
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_10(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(None, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_11(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, None):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_12(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_13(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, ):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_14(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(3, n + 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_15(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n - 1):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_16(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 2):
                a, b = b, a + b
            return b

    def xǁCalculatorǁfibonacci__mutmut_17(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = None
            return b

    def xǁCalculatorǁfibonacci__mutmut_18(self, n: int) -> int:
        """Calcula o n-ésimo número de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a - b
            return b
    
    xǁCalculatorǁfibonacci__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁfibonacci__mutmut_1': xǁCalculatorǁfibonacci__mutmut_1, 
        'xǁCalculatorǁfibonacci__mutmut_2': xǁCalculatorǁfibonacci__mutmut_2, 
        'xǁCalculatorǁfibonacci__mutmut_3': xǁCalculatorǁfibonacci__mutmut_3, 
        'xǁCalculatorǁfibonacci__mutmut_4': xǁCalculatorǁfibonacci__mutmut_4, 
        'xǁCalculatorǁfibonacci__mutmut_5': xǁCalculatorǁfibonacci__mutmut_5, 
        'xǁCalculatorǁfibonacci__mutmut_6': xǁCalculatorǁfibonacci__mutmut_6, 
        'xǁCalculatorǁfibonacci__mutmut_7': xǁCalculatorǁfibonacci__mutmut_7, 
        'xǁCalculatorǁfibonacci__mutmut_8': xǁCalculatorǁfibonacci__mutmut_8, 
        'xǁCalculatorǁfibonacci__mutmut_9': xǁCalculatorǁfibonacci__mutmut_9, 
        'xǁCalculatorǁfibonacci__mutmut_10': xǁCalculatorǁfibonacci__mutmut_10, 
        'xǁCalculatorǁfibonacci__mutmut_11': xǁCalculatorǁfibonacci__mutmut_11, 
        'xǁCalculatorǁfibonacci__mutmut_12': xǁCalculatorǁfibonacci__mutmut_12, 
        'xǁCalculatorǁfibonacci__mutmut_13': xǁCalculatorǁfibonacci__mutmut_13, 
        'xǁCalculatorǁfibonacci__mutmut_14': xǁCalculatorǁfibonacci__mutmut_14, 
        'xǁCalculatorǁfibonacci__mutmut_15': xǁCalculatorǁfibonacci__mutmut_15, 
        'xǁCalculatorǁfibonacci__mutmut_16': xǁCalculatorǁfibonacci__mutmut_16, 
        'xǁCalculatorǁfibonacci__mutmut_17': xǁCalculatorǁfibonacci__mutmut_17, 
        'xǁCalculatorǁfibonacci__mutmut_18': xǁCalculatorǁfibonacci__mutmut_18
    }
    
    def fibonacci(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁfibonacci__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁfibonacci__mutmut_mutants"), args, kwargs, self)
        return result 
    
    fibonacci.__signature__ = _mutmut_signature(xǁCalculatorǁfibonacci__mutmut_orig)
    xǁCalculatorǁfibonacci__mutmut_orig.__name__ = 'xǁCalculatorǁfibonacci'

    def xǁCalculatorǁcount_digits__mutmut_orig(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_1(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number != 0:
            return 1
        number = abs(number)
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_2(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 1:
            return 1
        number = abs(number)
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_3(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 2
        number = abs(number)
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_4(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = None
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_5(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(None)
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_6(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = None
        while number > 0:
            count += 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_7(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 1
        while number > 0:
            count += 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_8(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number >= 0:
            count += 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_9(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number > 1:
            count += 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_10(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number > 0:
            count = 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_11(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number > 0:
            count -= 1
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_12(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number > 0:
            count += 2
            number //= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_13(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number > 0:
            count += 1
            number = 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_14(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number > 0:
            count += 1
            number /= 10
        return count

    def xǁCalculatorǁcount_digits__mutmut_15(self, number: int) -> int:
        """Conta o número de dígitos em um número inteiro."""
        if number == 0:
            return 1
        number = abs(number)
        count = 0
        while number > 0:
            count += 1
            number //= 11
        return count
    
    xǁCalculatorǁcount_digits__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁcount_digits__mutmut_1': xǁCalculatorǁcount_digits__mutmut_1, 
        'xǁCalculatorǁcount_digits__mutmut_2': xǁCalculatorǁcount_digits__mutmut_2, 
        'xǁCalculatorǁcount_digits__mutmut_3': xǁCalculatorǁcount_digits__mutmut_3, 
        'xǁCalculatorǁcount_digits__mutmut_4': xǁCalculatorǁcount_digits__mutmut_4, 
        'xǁCalculatorǁcount_digits__mutmut_5': xǁCalculatorǁcount_digits__mutmut_5, 
        'xǁCalculatorǁcount_digits__mutmut_6': xǁCalculatorǁcount_digits__mutmut_6, 
        'xǁCalculatorǁcount_digits__mutmut_7': xǁCalculatorǁcount_digits__mutmut_7, 
        'xǁCalculatorǁcount_digits__mutmut_8': xǁCalculatorǁcount_digits__mutmut_8, 
        'xǁCalculatorǁcount_digits__mutmut_9': xǁCalculatorǁcount_digits__mutmut_9, 
        'xǁCalculatorǁcount_digits__mutmut_10': xǁCalculatorǁcount_digits__mutmut_10, 
        'xǁCalculatorǁcount_digits__mutmut_11': xǁCalculatorǁcount_digits__mutmut_11, 
        'xǁCalculatorǁcount_digits__mutmut_12': xǁCalculatorǁcount_digits__mutmut_12, 
        'xǁCalculatorǁcount_digits__mutmut_13': xǁCalculatorǁcount_digits__mutmut_13, 
        'xǁCalculatorǁcount_digits__mutmut_14': xǁCalculatorǁcount_digits__mutmut_14, 
        'xǁCalculatorǁcount_digits__mutmut_15': xǁCalculatorǁcount_digits__mutmut_15
    }
    
    def count_digits(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁcount_digits__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁcount_digits__mutmut_mutants"), args, kwargs, self)
        return result 
    
    count_digits.__signature__ = _mutmut_signature(xǁCalculatorǁcount_digits__mutmut_orig)
    xǁCalculatorǁcount_digits__mutmut_orig.__name__ = 'xǁCalculatorǁcount_digits'

    def xǁCalculatorǁis_prime__mutmut_orig(self, n: int) -> bool:
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

    def xǁCalculatorǁis_prime__mutmut_1(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n <= 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_2(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 3:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_3(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return True
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_4(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n != 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_5(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 3:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_6(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return False
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_7(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n / 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_8(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 3 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_9(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 != 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_10(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 1:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_11(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return True
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_12(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(None, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_13(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, None, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_14(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, None):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_15(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_16(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_17(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, ):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_18(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(4, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_19(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) - 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_20(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(None) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_21(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(None)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_22(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 2, 2):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_23(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 3):
            if n % i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_24(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n / i == 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_25(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i != 0:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_26(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 1:
                return False
        return True

    def xǁCalculatorǁis_prime__mutmut_27(self, n: int) -> bool:
        """Verifica se um número é primo."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return True
        return True

    def xǁCalculatorǁis_prime__mutmut_28(self, n: int) -> bool:
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
        return False
    
    xǁCalculatorǁis_prime__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁis_prime__mutmut_1': xǁCalculatorǁis_prime__mutmut_1, 
        'xǁCalculatorǁis_prime__mutmut_2': xǁCalculatorǁis_prime__mutmut_2, 
        'xǁCalculatorǁis_prime__mutmut_3': xǁCalculatorǁis_prime__mutmut_3, 
        'xǁCalculatorǁis_prime__mutmut_4': xǁCalculatorǁis_prime__mutmut_4, 
        'xǁCalculatorǁis_prime__mutmut_5': xǁCalculatorǁis_prime__mutmut_5, 
        'xǁCalculatorǁis_prime__mutmut_6': xǁCalculatorǁis_prime__mutmut_6, 
        'xǁCalculatorǁis_prime__mutmut_7': xǁCalculatorǁis_prime__mutmut_7, 
        'xǁCalculatorǁis_prime__mutmut_8': xǁCalculatorǁis_prime__mutmut_8, 
        'xǁCalculatorǁis_prime__mutmut_9': xǁCalculatorǁis_prime__mutmut_9, 
        'xǁCalculatorǁis_prime__mutmut_10': xǁCalculatorǁis_prime__mutmut_10, 
        'xǁCalculatorǁis_prime__mutmut_11': xǁCalculatorǁis_prime__mutmut_11, 
        'xǁCalculatorǁis_prime__mutmut_12': xǁCalculatorǁis_prime__mutmut_12, 
        'xǁCalculatorǁis_prime__mutmut_13': xǁCalculatorǁis_prime__mutmut_13, 
        'xǁCalculatorǁis_prime__mutmut_14': xǁCalculatorǁis_prime__mutmut_14, 
        'xǁCalculatorǁis_prime__mutmut_15': xǁCalculatorǁis_prime__mutmut_15, 
        'xǁCalculatorǁis_prime__mutmut_16': xǁCalculatorǁis_prime__mutmut_16, 
        'xǁCalculatorǁis_prime__mutmut_17': xǁCalculatorǁis_prime__mutmut_17, 
        'xǁCalculatorǁis_prime__mutmut_18': xǁCalculatorǁis_prime__mutmut_18, 
        'xǁCalculatorǁis_prime__mutmut_19': xǁCalculatorǁis_prime__mutmut_19, 
        'xǁCalculatorǁis_prime__mutmut_20': xǁCalculatorǁis_prime__mutmut_20, 
        'xǁCalculatorǁis_prime__mutmut_21': xǁCalculatorǁis_prime__mutmut_21, 
        'xǁCalculatorǁis_prime__mutmut_22': xǁCalculatorǁis_prime__mutmut_22, 
        'xǁCalculatorǁis_prime__mutmut_23': xǁCalculatorǁis_prime__mutmut_23, 
        'xǁCalculatorǁis_prime__mutmut_24': xǁCalculatorǁis_prime__mutmut_24, 
        'xǁCalculatorǁis_prime__mutmut_25': xǁCalculatorǁis_prime__mutmut_25, 
        'xǁCalculatorǁis_prime__mutmut_26': xǁCalculatorǁis_prime__mutmut_26, 
        'xǁCalculatorǁis_prime__mutmut_27': xǁCalculatorǁis_prime__mutmut_27, 
        'xǁCalculatorǁis_prime__mutmut_28': xǁCalculatorǁis_prime__mutmut_28
    }
    
    def is_prime(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁis_prime__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁis_prime__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_prime.__signature__ = _mutmut_signature(xǁCalculatorǁis_prime__mutmut_orig)
    xǁCalculatorǁis_prime__mutmut_orig.__name__ = 'xǁCalculatorǁis_prime'