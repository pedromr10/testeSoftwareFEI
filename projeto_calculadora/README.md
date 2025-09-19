# Como usar o código
## Instalar o coverage:
pip install -r requirements.txt

## Executando os testes:
```
python -m unittest discover tests -v
```

## Executando com cobertura:
```
coverage run -m unittest discover tests
coverage report
coverage html
```

## Executando testes especficos:
```
python -m unittest tests.test_unidade.TestCalculadora.test_soma -v
```

## Observações
* Os testes foram realizados em um virtual environment (venv)
### Como criar uma venv:
```
python -m venv nomeDaVenv
```

### Para acessar a venv:
```
.\nomeDaVenv\Scripts\activate
```

### Para sair da venv:
```
deactivate
```
