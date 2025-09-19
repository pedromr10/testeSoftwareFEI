# Relatório laboratório 5 - CC8550

## Integrantes:
* Fernando Milani | 24.122.063-1
* Gustavo Gomes Barbosa | 24.122.061-5
* Murilo Darce | 24.122.031-8
* Pedro Munhoz Rosin | 24.122.013-6

## Testes realizados:

### Observações:
* Código utilizado para executar os testes:
"python -m unittest discover tests -v";
* Código utilizado para obter a cobertura do código: "coverage run -m unittest discover tests" e
"coverage report";
* Alguns testes extras foram criados com o objetivo de ter um resultado anômalo, errado, para realizar o debug do programa.

### Resultado da execução dos testes:
test_integracao_historico_resultado (test_integracao.TestIntegracaoCalculadora) ... ok <br>
test_operacoes_sequenciais (test_integracao.TestIntegracaoCalculadora) ... ok <br>
test_integracao_historico_resultado_extra (test_integracao_extra.TestIntegracaoCalculadoraExtra) ... FAIL <br>
test_operacoes_sequenciais_extra (test_integracao_extra.TestIntegracaoCalculadoraExtra) ... FAIL <br>
test_consistencia_historico (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_divisao_por_zero (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_entrada_saida_divisao (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_entrada_saida_multiplicacao (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_entrada_saida_soma (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_entrada_saida_subtracao (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_fluxos_divisao (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_inicializacao (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_limite_inferior (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_limite_superior (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_mensagens_erro (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_modificacao_historico (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_tipagem_invalida (test_unidade.TestUnidadeCalculadora) ... ok <br>
test_consistencia_historico_extra (test_unidade_extra.TestUnidadeCalculadoraExtra) ... FAIL <br>
test_divisao_por_zero (test_unidade_extra.TestUnidadeCalculadoraExtra) ... ok <br>
test_entrada_saida_extra (test_unidade_extra.TestUnidadeCalculadoraExtra) ... ERROR <br>
test_fluxos_divisao (test_unidade_extra.TestUnidadeCalculadoraExtra) ... ok <br>
test_inicializacao (test_unidade_extra.TestUnidadeCalculadoraExtra) ... ok <br>
test_limite_inferior (test_unidade_extra.TestUnidadeCalculadoraExtra) ... ok <br>
test_limite_superior (test_unidade_extra.TestUnidadeCalculadoraExtra) ... ok <br>
test_mensagens_erro (test_unidade_extra.TestUnidadeCalculadoraExtra) ... ERROR <br>
test_modificacao_historico (test_unidade_extra.TestUnidadeCalculadoraExtra) ... ok <br>
test_tipagem_invalida_extra (test_unidade_extra.TestUnidadeCalculadoraExtra) ... FAIL <br>

Ran 27 tests in 0.003s

FAILED (failures=4, errors=2)

### Cobertura dos testes:

| Name                             | Stmts | Miss | Cover |
|----------------------------------|-------|------|-------|
| src\calculadora.py               | 47    | 1    | 98%   |
| tests\test_integracao.py         | 31    | 1    | 97%   |
| tests\test_integracao_extra.py   | 33    | 8    | 76%   |
| tests\test_unidade.py            | 112   | 1    | 99%   |
| tests\test_unidade_extra.py      | 99    | 11   | 89%   |
|----------------------------------|-------|------|-------|
| TOTAL                            | 322   | 22   | 93%   |

### Problemas encontrados e soluções obtidas:

#### Resultado de falhas: <br>
FAILED (failures=4, errors=2)

#### Foram encontrados problemas como:
* TypeError: Argumentos devem ser numeros
* AssertionError: 3164.0625 != 56.25
* AssertionError: '144 / 12 = 12' not found in ['145 + 378 = 523', '982 - 467 = 515', '23 * 17 = 391', '144 / 12 = 12.0', '5 ^ 4 = 625']
* AssertionError: TypeError not raised

#### Soluções:
Os problemas citados foram criados para serem anômalos, apenas para debug. Desta maneira, não foram necessárias correções, uma vez que os testes de assertividade obtiveram respostas positivas.

### Lições aprendidas sobre cada tipo de teste:

Cada tipo de teste possui sua importância, quando visto por um todo. Nenhum é mais ou menos importante que outro, uma vez que todos precisam estar funcionando para que o sistema consiga fluir normalmente e de forma desejada.


- 4.1 Teste de Operações Sequenciais
Esse teste executa uma sequência de operações encadeadas (2 + 3 = 5 → 5 * 4 = 20 -> 20 / 2 = 10)
O resultado final esperado é 10, e o teste também confirma que o histórico possui exatamente 3 registros correspondentes às operações realizadas.
- 4.2 Teste de Interface entre Métodos
Esse teste verifica se métodos diferentes conseguem se comunicar via obter_ultimo_resultado.
Primeiro é feita uma potência (2 ^3 = 8) e em seguida, o resultado é usado como entrada em outra operação (8 + 2 = 10)
O teste garante que o valor final armazenado é 10 e que o histórico contém os registros certos

Os testes de integração confirmaram que a calculadora mantém a consistência de resultados e histórico quando operações são executadas em conjunto. Além disso, mostraram que os métodos se integram corretamente por meio do compartilhamento do último resultado.
