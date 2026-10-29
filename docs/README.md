\# 📋 Documentação de Conformidade \& ISO 27001



> Este diretório armazena as diretrizes de governança, políticas de segurança da informação e os padrões de conformidade adotados no \*\*Cybersecurity Incident \& Compliance Tracker\*\*.



\---



\## 🛡️ Diretrizes e Alinhamento com a ISO 27001



O sistema foi arquitetado para apoiar organizações no cumprimento de requisitos fundamentais da norma \*\*ISO/IEC 27001\*\*, com foco especial nas seguintes seções de controle:



\### 1. A.9 – Controle de Acesso

\* \*\*Objetivo:\*\* Restringir o acesso a informações e aos recursos de processamento de informações.

\* \*\*Implementação no Projeto:\*\* 

&#x20; \* Monitoramento contínuo de tentativas de autenticação (`LOGIN\_SUCCESS` e `LOGIN\_FAILED`).

&#x20; \* Registro de IPs de origem e categorização de usuários por nível de risco e privilégio (Administrador, Analista, Operacional).



\### 2. A.12 – Segurança nas Operações

\* \*\*Objetivo:\*\* Garantir a operação correta e segura das facilidades de processamento de informação.

\* \*\*Implementação no Projeto:\*\*

&#x20; \* Rastreamento automatizado de eventos anômalos e tentativas de acesso de locais não reconhecidos ou IPs externos suspeitos.

&#x20; \* Validação de logs operacionais integrados ao banco de dados SQLite.



\### 3. A.16 – Gestão de Incidentes de Segurança da Informação

\* \*\*Objetivo:\*\* Assecruar uma abordagem consistente e eficaz para a gestão de incidentes de segurança da informação.

\* \*\*Implementação no Projeto:\*\*

&#x20; \* Painel de SOC para triagem de incidentes por severidade (\*Baixa, Média, Alta, Crítica\*).

&#x20; \* Acompanhamento de status de resolução (\*Aberto, Em Investigação, Resolvido\*) e conformidade com métricas de SLA (\*MTTD\* e \*MTTR\*).



\---



\## ⏱️ SLAs de Resposta a Incidentes (SOC)



Para manter a conformidade regulatória, os incidentes detectados pelo sistema seguem os seguintes tempos máximos de resposta:

\* \*\*Crítica:\*\* Investigação imediata / Contenção em até \*\*1 hora\*\*.

\* \*\*Alta:\*\* Contenção em até \*\*4 horas\*\*.

\* \*\*Média / Baixa:\*\* Tratamento dentro do ciclo operacional diário.



\---

\*Compliance \& Security Governance | Projeto de Portfólio 2026\*

