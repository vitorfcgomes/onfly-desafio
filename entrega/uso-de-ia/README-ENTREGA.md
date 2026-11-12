
# Documentação da entrega — Desafio Onfly

## Objetivo

Registrar as atividades realizadas durante a análise, correção e validação do desafio técnico Python.

O projeto trabalha com leitura de reservas em CSV, processamento de dados e geração de relatórios JSON.

## Metodologia

A resolução foi conduzida de maneira incremental:

- Análise dos requisitos.
- Reprodução dos defeitos.
- Investigação das causas.
- Implementação das correções.
- Testes automatizados.
- Verificação de regressões.
- Documentação do uso de inteligência artificial.

## Correções realizadas

| Componente | Problema | Situação |
|---|---|---|
| Repositório CSV | Limite de 200 registros | Corrigido |
| Conversão cambial | Operação matemática incorreta | Corrigido |
| Cálculo de noites | Diferença de datas incorreta | Corrigido |
| Regras de status | Inclusão indevida de reservas no faturamento | Pendente |
| Ranking de hotéis | Ordenação incorreta | Pendente |
| Relatório de regressão | Divergência nos valores agregados | Pendente de revalidação |

## Testes validados individualmente

- `test_repository_reads_all_reservations_and_parses_record_250` — PASSED.
- `test_currency_conversion_to_brl` — PASSED.
- `test_nights_across_month_boundary` — PASSED.

## Próximas etapas

1. Corrigir as regras de status.
2. Corrigir o ranking de hotéis.
3. Revalidar o relatório de regressão.
4. Executar a suíte completa.
5. Registrar os resultados finais.

## Utilização de IA

As interações com inteligência artificial estão documentadas em `uso-de-ia/`, incluindo o histórico das sessões e a declaração de utilização da ferramenta.

As alterações no código foram realizadas e validadas pelo desenvolvedor.
