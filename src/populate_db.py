import sqlite3
from datetime import datetime, timedelta
import random

def populate_database():
    db_path = "data/security_hub.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Limpa dados antigos se houver
    cursor.execute("DELETE FROM assets_users")
    cursor.execute("DELETE FROM access_logs")
    cursor.execute("DELETE FROM security_incidents")
    
    # 1. Inserir Usuários
    users = [
        ("carlos.silva", "TI Infra", "Administrador", "Médio"),
        ("ana.souza", "Financeiro", "Analista Sênior", "Baixo"),
        ("marcos.lima", "Comercial", "Executivo de Vendas", "Baixo"),
        ("beatriz.alves", "RH", "Gerente", "Baixo"),
        ("root_admin", "Segurança", "Super User", "Alto")
    ]
    cursor.executemany("INSERT INTO assets_users (username, department, role, risk_level) VALUES (?, ?, ?, ?)", users)
    
    # 2. Gerar Logs de Acesso Simulados
    actions = ["LOGIN_SUCCESS", "LOGIN_FAILED", "PASSWORD_RESET", "PRIVILEGE_ESCALATION"]
    ips = ["192.168.1.15", "10.0.4.52", "177.185.90.11", "45.33.32.156", "192.168.1.102"]
    locations = ["Guarapari - BR", "Vitória - BR", "São Paulo - BR", "IP Estrangeiro (Desconhecido)", "Rio de Janeiro - BR"]
    
    base_time = datetime.now() - timedelta(days=7)
    
    log_records = []
    for i in range(250):
        current_time = base_time + timedelta(hours=random.randint(0, 168), minutes=random.randint(0, 59))
        user = random.choice(users)[0]
        ip = random.choice(ips)
        loc = locations[0] if "192.168" in ip or "10.0" in ip else locations[3]
        
        # Simula anomalia para IP estrangeiro
        if "Estrangeiro" in loc:
            action = "LOGIN_FAILED"
            status = "SUSPICIOUS"
        else:
            action = random.choices(actions, weights=[70, 20, 5, 5])[0]
            status = "SUCCESS" if action != "LOGIN_FAILED" else "BLOCKED"
            
        log_records.append((current_time.strftime("%Y-%m-%d %H:%M:%S"), ip, user, action, status, loc))
        
    cursor.executemany("""
        INSERT INTO access_logs (timestamp, ip_address, username, action, status, location)
        VALUES (?, ?, ?, ?, ?, ?)
    """, log_records)
    
    # 3. Inserir Incidentes de Segurança
    incidents = [
        ("INC-2026-001", "2026-10-20 03:14:22", "Brute Force", "Alta", "Resolvido", "2026-10-20 04:30:00", "Carlos Silva"),
        ("INC-2026-002", "2026-10-22 23:45:10", "Unauthorized Access", "Crítica", "Em Investigação", None, "Equipe SOC"),
        ("INC-2026-003", "2026-10-25 14:12:05", "Malware Alert", "Média", "Aberto", None, "Carlos Silva"),
    ]
    cursor.executemany("""
        INSERT INTO security_incidents (incident_id, detected_at, incident_type, severity, status, resolved_at, assigned_to)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, incidents)
    
    conn.commit()
    conn.close()
    print("[INFO] Banco de dados populado com sucesso com usuários, logs e incidentes simulados!")

if __name__ == "__main__":
    populate_database()