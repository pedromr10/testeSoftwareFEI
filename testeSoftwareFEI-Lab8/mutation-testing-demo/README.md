# Mutation Testing Demo

Um projeto educacional demonstrando testes de mutação em Python usando a ferramenta `mutmut`.

## Sobre o Projeto

Este projeto foi desenvolvido para ensinar os conceitos de **testes de mutação** através de exemplos práticos. Os testes de mutação são uma técnica avançada que avalia a qualidade de uma suíte de testes introduzindo pequenas alterações (mutações) no código e verificando se os testes conseguem detectá-las.

**Nota importante**: Esta versão contém intencionalmente uma suíte de testes com lacunas para fins educacionais, permitindo que mutantes sobrevivam e sejam analisados pelos estudantes.

## Estrutura do Projeto

```
mutation-testing-demo/
├── README.md
├── requirements.txt
├── setup.cfg
├── .gitignore
├── calculator/
│   ├── __init__.py
│   └── operations.py
└── tests/
    ├── __init__.py
    └── test_operations.py
```

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Git

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Rossi-Luciano/teste_de_software.git
   cd teste_de_software/mutation-testing-demo
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   
   # Linux/Mac
   source venv/bin/activate
   
   # Windows
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

### 1. Executar Testes Normais

Primeiro, verifique se todos os testes passam:

```bash
python -m pytest tests/ -v
```

**Saída esperada:**
```
========================================================================================== test session starts ===========================================================================================
platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.5.0
rootdir: /workspaces/mutation-testing-demo
configfile: setup.cfg
plugins: cov-7.0.0
collected 12 items

tests/test_operations.py::TestCalculator::test_add PASSED                                  [  8%]
tests/test_operations.py::TestCalculator::test_multiply PASSED                             [ 16%]
tests/test_operations.py::TestCalculator::test_divide_zero PASSED                          [ 25%]
tests/test_operations.py::TestCalculator::test_square_root_negative PASSED                 [ 33%]
tests/test_operations.py::TestCalculator::test_factorial_negative PASSED                   [ 41%]
tests/test_operations.py::TestCalculator::test_absolute_value_basic PASSED                 [ 50%]
tests/test_operations.py::TestCalculator::test_max_of_two_equal PASSED                     [ 58%]
tests/test_operations.py::TestCalculator::test_is_positive_true PASSED                     [ 66%]
tests/test_operations.py::TestCalculator::test_calculate_percentage_basic PASSED           [ 75%]
tests/test_operations.py::TestCalculator::test_grade_classification_a PASSED               [ 83%]
tests/test_operations.py::TestCalculator::test_fibonacci_base_case PASSED                  [ 91%]
tests/test_operations.py::TestCalculator::test_is_prime_true_case PASSED                   [100%]

=========================================================================================== 12 passed in 0.04s ===========================================================================================
```

### 2. Verificar Cobertura de Código

```bash
python -m pytest --cov=calculator/ tests/
```

**Saída esperada:**
```
============================================================================================= tests coverage =============================================================================================
Name                       Stmts   Miss  Cover
----------------------------------------------
calculator/__init__.py         3      0   100%
calculator/operations.py     101     53    48%
----------------------------------------------
TOTAL                        104     53    49%
=========================================================================================== 12 passed in 0.11s ===========================================================================================
```

**Observação importante**: Apesar da cobertura de apenas 49%, todos os testes passam. Isso demonstra uma limitação da métrica de cobertura.

### 3. Executar Testes de Mutação

```bash
# Remover cache anterior (se existir)
rm -rf .mutmut-cache/

# Executar mutmut
mutmut run
```

**Saída esperada:**
```
⠋ Generating mutants
    done in 2ms
⠇ Listing all tests 
⠴ Running clean tests
    done
⠏ Running forced fail test
    done
Running mutation testing
⠸ 123/123  🎉 80 🫥 43  ⏰ 0  🤔 0  🙁 0  🔇 0
0.00 mutations/second
```

### 4. Visualizar Resultados

```bash
# Ver resumo dos resultados
mutmut results
```

**Saída esperada (parcial):**
```
    calculator.operations.xǁCalculatorǁsubtract__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁpower__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁis_even__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁis_even__mutmut_2: no tests
    calculator.operations.xǁCalculatorǁis_even__mutmut_3: no tests
    calculator.operations.xǁCalculatorǁis_even__mutmut_4: no tests
    calculator.operations.xǁCalculatorǁmin_of_three__mutmut_1: no tests
    calculator.operations.xǁCalculatorǁmin_of_three__mutmut_2: no tests
    ...
    calculator.operations.xǁCalculatorǁcount_digits__mutmut_15: no tests
```

### 5. Analisar Mutantes Específicos

```bash
# Analisar um mutante específico
mutmut show "calculator.operations.xǁCalculatorǁsubtract__mutmut_1"
```

**Saída esperada:**
```
# calculator.operations.xǁCalculatorǁsubtract__mutmut_1: no tests
--- calculator/operations.py
+++ calculator/operations.py
@@ -1,3 +1,3 @@
 def subtract(self, a: Number, b: Number) -> Number:
         """Subtrai dois números."""
-        return a - b
+        return a + b
```

### 6. Interpretar os Resultados

**Símbolos dos Resultados:**
- 🎉 **80 killed**: Testes detectaram essas mutações
- 🫥 **43 survived**: Mutações não detectadas pelos testes
- ⏰ **0 timeout**: Nenhuma mutação causou execução lenta
- 🤔 **0 incompetent**: Nenhuma mutação causou erro de sintaxe

**Taxa de Mutação Atual:**
```
Taxa = 80 killed / 123 total = 65%
```

## Análise dos Mutantes Sobreviventes

### Funções Completamente Não Testadas
- `subtract` (1 mutante)
- `power` (1 mutante)
- `is_even` (4 mutantes)
- `min_of_three` (4 mutantes)
- `compare_numbers` (5 mutantes)
- `is_in_range` (2 mutantes)
- `calculate_discount` (11 mutantes)
- `count_digits` (15 mutantes)

### Exemplo de Análise de Mutante

Para o mutante `subtract__mutmut_1`:
- **Tipo**: Operador aritmético (- → +)
- **Status**: Sobreviveu (no tests)
- **Motivo**: Função `subtract` não possui testes
- **Solução**: Adicionar teste como `assert calc.subtract(5, 3) == 2`

## Exercício Prático

### Fase 1: Análise Inicial (Estado Atual)
```
Cobertura de Código: 49%
Taxa de Mutação: 65%
Mutantes Sobreviventes: 43
```

### Fase 2: Adicionar Testes
Adicione testes para as funções não cobertas:

```python
def test_subtract(self):
    assert self.calc.subtract(5, 3) == 2
    assert self.calc.subtract(1, 1) == 0

def test_is_even(self):
    assert self.calc.is_even(2) is True
    assert self.calc.is_even(3) is False
```

### Fase 3: Re-executar e Comparar
```bash
rm -rf .mutmut-cache/
mutmut run
```

**Meta Final:**
```
Cobertura de Código: >90%
Taxa de Mutação: >80%
Mutantes Sobreviventes: <10
```

## Comandos de Depuração

```bash
# Ver diferenças após aplicar mutante
mutmut apply "calculator.operations.xǁCalculatorǁsubtract__mutmut_1"
git diff
python -m pytest tests/ -v
git checkout -- calculator/

# Verificar sintaxe
python -c "import calculator.operations"

# Executar teste específico
python -m pytest tests/test_operations.py::TestCalculator::test_add -v
```

## Tipos de Mutações Encontradas

- **Operadores aritméticos**: `+` ↔ `-`, `*` ↔ `/`
- **Operadores relacionais**: `>` ↔ `>=`, `<` ↔ `<=`, `==` ↔ `!=`
- **Operadores lógicos**: `and` ↔ `or`
- **Valores literais**: `0` ↔ `1`, `2` ↔ `3`
- **Condições de fronteira**: limites de loops e ranges

## Objetivos Educacionais

Este projeto demonstra:

1. **Limitações da cobertura de código**: 49% de cobertura mas testes passam
2. **Valor dos testes de mutação**: Revelam lacunas reais (65% vs. 100%)
3. **Análise sistemática**: Como identificar e corrigir lacunas específicas
4. **Melhoria iterativa**: Processo de aumento da qualidade dos testes

## Troubleshooting

### Problema: Comando `mutmut show` falha
**Solução**: Use o nome completo exato conforme mostrado em `mutmut results`

### Problema: Cache antigo interferindo
**Solução**: Execute `rm -rf .mutmut-cache/` antes de `mutmut run`

### Problema: Testes falhando inesperadamente
**Solução**: Verifique se não há mutante aplicado com `git status`

## Recursos Adicionais

- [Documentação do mutmut](https://mutmut.readthedocs.io/)
- [Artigo original sobre Mutation Testing](https://dl.acm.org/doi/10.1145/360248.360252)
- [Pytest Documentation](https://docs.pytest.org/)

## Licença

Este projeto está licenciado sob a MIT License.

## Autor

- **Prof. Luciano Rossi** - Centro Universitário FEI
- Disciplina: Simulação e Teste de Software (CC8550)
