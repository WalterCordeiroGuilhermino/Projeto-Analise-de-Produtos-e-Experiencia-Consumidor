Este projeto surgiu de um case e um dataset hipotético compartilhado por **Ali Ahmad**. 

O objetivo foi criar um dashboard de análise de marketing para a **ShopEasy**, uma empresa de varejo online que enfrenta desafios com engajamento do cliente e taxas de conversão.

## Objetivo do Projeto
- Analisar métricas de engajamento (visualizações, cliques e likes) para entender o comportamento do cliente.
- Monitorar a taxa de conversão e a nota dos clientes ao longo do tempo.
- Realizar análise de sentimento a partir das notas dos clientes.
- Identificar tendências mensais e segmentar dados por ano, mês e produto.

## KPIs e Métricas Analisadas
- **Métricas de Engajamento**:
  - Visualizações
  - Cliques
  - Likes
- **Taxa de Conversão**
- **Nota dos Clientes** (Feedback Score)
- **Análise de Sentimento**:
  - Utilização da biblioteca **VADER** (Valence Aware Dictionary and sEntiment Reasoner) para análise de sentimentos a partir das notas dos clientes.
- **Análise Mensal**:
  - Tendências de engajamento e conversão ao longo dos meses.
- **Filtros**:
  - Por ano, mês e produto.

## Ferramentas Utilizadas
- **Microsoft SQL Server Management Studio (SSMS)**: Para limpeza e preparação dos dados.
- **Python**: Para análise de sentimentos utilizando a biblioteca **VADER**.
- **Power BI**: Para criação do dashboard e relacionamento entre os dados.

## Estrutura do Dashboard
O dashboard é dividido em três seções principais:
1. **Engajamento do Cliente**:
   - Visualizações, cliques e likes ao longo do tempo.
   - Análise mensal e por produto.
2. **Taxa de Conversão**:
   - Monitoramento da taxa de conversão mensal.
   - Identificação de tendências e gargalos.
3. **Feedback dos Clientes**:
   - Nota média dos clientes.
   - Análise de sentimentos (positivo, negativo, neutro) utilizando VADER.
   - Análise mensal e por produto.