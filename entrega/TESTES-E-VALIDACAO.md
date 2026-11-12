# Testes e Validação

## Objetivo

Documentar como validar as correções do consolidador de reservas e como repetir a suíte de testes antes de cada entrega.

## Execução

A partir da raiz do projeto, com o ambiente virtual ativado:

```powershell
python -m pytest -v
```

Para interromper no primeiro erro:

```powershell
python -m pytest -x
```

Para obter um resumo mais curto:

```powershell
python -m pytest -q
```

## Cobertura funcional registrada

| Arquivo de teste | Responsabilidade a validar |
|---|---|
| `test_csv_reservation_repository.py` | Leitura do CSV e quantidade de registros |
| `test_currency.py` | Conversão de moedas e precisão monetária |
| `test_nights.py` | Cálculo da quantidade de noites |
| `test_status_rules.py` | Regras de faturamento por status |
| `test_top_hotels.py` | Ordenação e desempate do ranking |
| `test_regression_report.py` | Comportamento integrado do relatório |

Os nomes indicam a área principal de cada suíte; consulte os próprios testes para confirmar os cenários e asserts efetivamente implementados.

## Cenários importantes

- Valores monetários devem evitar erros de precisão binária.
- Datas em meses ou anos diferentes não podem produzir quantidade incorreta de noites.
- Reservas `NO_SHOW` não devem ser faturadas, conforme a regra de negócio adotada.
- O ranking deve priorizar os maiores valores e manter desempate determinístico.
- A leitura não deve truncar o arquivo ao atingir 200 linhas.
- O relatório integrado deve permanecer consistente após as correções.

## Registro da execução final

Preencha após executar os testes localmente:

```text
Data:
Python:
Comando:
Testes coletados:
Aprovados:
Falharam:
Ignorados:
Observações:
```

Não declare cobertura percentual sem executar uma ferramenta de cobertura, como `pytest-cov`.
