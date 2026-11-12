# Sessão 01 — Diagnóstico inicial do desafio Onfly

**Data:** 12/11/2026  
**Ferramenta de apoio:** ChatGPT  
**Modelo informado na sessão:** GPT-6

## Objetivo

Compreender a arquitetura do projeto, identificar requisitos funcionais e reproduzir defeitos antes de alterar a implementação.

## Abordagem

A análise começou pela estrutura do projeto e pela identificação dos módulos responsáveis por leitura dos dados, regras de negócio e geração do relatório.

Foi adotada a decisão de investigar os problemas em um ambiente de testes, evitando realizar alterações sem uma forma de verificar o comportamento.

## Princípio de engenharia

A correção deve preservar a lógica principal da aplicação. Para isso, é necessário reproduzir o defeito, entender sua causa, implementar uma mudança localizada e executar os testes de regressão.

## Resultado da sessão

Foram identificadas áreas que precisavam de investigação: precisão monetária, cálculo de noites, regra de faturamento por status, ordenação do ranking e limite de registros na leitura CSV.

## Aprendizado

Testes automatizados funcionam como uma rede de segurança: permitem verificar se uma correção resolve o defeito sem introduzir regressões em funcionalidades existentes.
