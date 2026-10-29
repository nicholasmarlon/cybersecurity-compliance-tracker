import sqlite3
import pandas as pd

def analyze_security_data():
    db_path = "data/security_hub.db"
    conn = sqlite3.connect(db_path)
    
    print("=" * 60)
    print("🛡️  RELATÓRIO DE ANÁLISE DE SEGURANÇA E COMPLIANCE - SOC")
    print("=" * 60)
    
    # 1. Carregar logs de acesso
    df_logs = pd.read_sql("SELECT * FROM access_logs", conn)
    
    total_events = len(df_logs)
    failed_logins = len(df_logs[df_logs['action'] == 'LOGIN_FAILED'])
    suspicious_events = len(df_logs[df_logs['status'] == 'SUSPICIOUS'])
    
    print(f"\n[📊] MÉTRICAS GERAIS DE ACESSO:")
    print(f" • Total de Eventos de Log Analisados: {total_events}")
    print(f" • Total de Falhas de Autenticação: {failed_logins}")
    print(f" • Eventos Marcados como Suspeitos: {suspicious_events}")
    
    # 2. Identificar IPs com maior número de falhas (Possível Brute Force)
    print(f"\n[🔍] TOP IPs COM TENTATIVAS SUSPEITAS / FALHAS:")
    top_ips = df_logs[df_logs['status'].isin(['BLOCKED', 'SUSPICIOUS'])].groupby('ip_address').size().reset_index(name='count')
    top_ips = top_ips.sort_values(by='count', ascending=False)
    for index, row in top_ips.iterrows():
        print(f" • IP: {row['ip_address']} | Alertas: {row['count']} ocorrências")
        
    # 3. Carregar Incidentes de Segurança
    df_incidents = pd.read_sql("SELECT * FROM security_incidents", conn)
    open_incidents = len(df_incidents[df_incidents['status'] != 'Resolvido'])
    
    print(f"\n[🚨] STATUS DOS INCIDENTES DE SEGURANÇA:")
    print(f" • Total de Incidentes Registrados: {len(df_incidents)}")
    print(f" • Incidentes Ativos/Em Investigação: {open_incidents}")
    
    print("\n" + "-" * 60)
    print("Análise concluída com sucesso!")
    print("=" * 60)
    
    conn.close()

if __name__ == "__main__":
    analyze_security_data()