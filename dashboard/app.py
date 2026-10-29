import streamlit as st
import sqlite3
import pandas as pd

# Configuração da Página
st.set_page_config(
    page_title="Cybersecurity & Compliance Hub",
    page_icon="🛡️",
    layout="wide"
)

# Função para conectar ao banco
def load_data():
    conn = sqlite3.connect("data/security_hub.db")
    df_logs = pd.read_sql("SELECT * FROM access_logs", conn)
    df_incidents = pd.read_sql("SELECT * FROM security_incidents", conn)
    df_assets = pd.read_sql("SELECT * FROM assets_users", conn)
    conn.close()
    return df_logs, df_incidents, df_assets

df_logs, df_incidents, df_assets = load_data()

# Cabeçalho Principal
st.title("🛡️ Cybersecurity Incident & Compliance Tracker")
st.markdown("Painel de Monitoramento de Operações de Segurança (SOC) e Governança de Acessos.")
st.markdown("---")

# Métricas Principais (KPIs)
total_events = len(df_logs)
failed_logins = len(df_logs[df_logs['action'] == 'LOGIN_FAILED'])
suspicious_events = len(df_logs[df_logs['status'] == 'SUSPICIOUS'])
open_incidents = len(df_incidents[df_incidents['status'] != 'Resolvido'])

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total de Logs de Acesso", value=total_events)
with col2:
    st.metric(label="Falhas de Autenticação", value=failed_logins, delta=f"-{(failed_logins/total_events)*100:.1f}% vs total" if total_events > 0 else "0")
with col3:
    st.metric(label="Eventos Suspeitos / IPs", value=suspicious_events, delta_color="inverse")
with col4:
    st.metric(label="Incidentes em Aberto", value=open_incidents, delta_color="inverse")

st.markdown("---")

# Abas de Navegação
tab1, tab2, tab3 = st.tabs(["📊 Monitoramento de Logs", "🚨 Gestão de Incidentes (SOC)", "👥 Ativos e Usuários"])

with tab1:
    st.subheader("Filtros e Visualização de Eventos de Acesso")
    
    status_filter = st.selectbox("Filtrar por Status do Evento:", options=["Todos"] + list(df_logs['status'].unique()))
    
    if status_filter != "Todos":
        filtered_df = df_logs[df_logs['status'] == status_filter]
    else:
        filtered_df = df_logs
        
    st.dataframe(filtered_df, use_container_width=True)
    
    st.markdown("### 📍 Ocorrências por Endereço IP")
    ip_counts = df_logs['ip_address'].value_counts().reset_index()
    ip_counts.columns = ['IP Address', 'Quantidade']
    st.bar_chart(ip_counts.set_index('IP Address'))

with tab2:
    st.subheader("Painel de Resposta a Incidentes")
    st.dataframe(df_incidents, use_container_width=True)
    
    st.info("💡 **Dica de Governança (ISO 27001):** Todos os incidentes críticos devem ser investigados e contatados dentro do SLA de até 4 horas.")

with tab3:
    st.subheader("Controle de Usuários e Níveis de Risco")
    st.dataframe(df_assets, use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("🔒 *Cybersecurity Hub | Desenvolvido com Python, SQLite e Streamlit.*")