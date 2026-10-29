\# 🛡️ Cybersecurity Incident \& Compliance Tracker



> Um sistema integrado de \*\*Security Operations Center (SOC)\*\* e \*\*Governança de Conformidade\*\* desenvolvido para monitoramento de eventos de autenticação, detecção de ameaças e rastreamento de incidentes de segurança.



\---



\## 🚀 Sobre o Projeto

O \*\*Cybersecurity Incident \& Compliance Tracker\*\* simula um ambiente corporativo voltado para a segurança da informação. O projeto une a engenharia de dados à análise preditiva de ameaças, centralizando o rastreamento de tentativas de \*Brute Force\*, mapeamento de acessos suspeitos por geolocalização/IP e o controle de SLAs de resposta a incidentes sob diretrizes de conformidade.



\---



\## 🛠️ Tecnologias e Ferramentas Utilizadas

\* \*\*Linguagem:\*\* Python

\* \*\*Manipulação \& Análise de Dados:\*\* Pandas

\* \*\*Banco de Dados \& SQL:\*\* SQLite (Modelagem Relacional de Logs e Incidentes)

\* \*\*Visualização \& Dashboard Interativo:\*\* Streamlit

\* \*\*Governança \& Segurança:\*\* Padrões de SOC, Métricas MTTD/MTTR e Conformidade (ISO 27001 / LGPD)

\* \*\*Controle de Versão:\*\* Git \& GitHub



\---



\## 📂 Arquitetura do Repositório



```text

cybersecurity-compliance-tracker/

│

├── data/                  # Banco de dados SQLite (security\_hub.db)

├── notebooks/             # Jupyter Notebooks para análise exploratória de logs

│   └── README.md

├── src/                   # Scripts de ETL, criação de banco e análise de risco

│   ├── create\_db.py       # Estruturação das tabelas relacionais de SOC

│   ├── populate\_db.py     # Geração de dados simulados (Mock Data de ameaças)

│   └── risk\_analyzer.py   # Motor de detecção de anomalias e relatórios de terminal

├── dashboard/             # Aplicação web interativa

│   └── app.py             # Dashboard executivo em Streamlit

├── docs/                  # Documentações de políticas e conformidade

│   └── README.md

└── README.md              # Documentação principal do projeto

