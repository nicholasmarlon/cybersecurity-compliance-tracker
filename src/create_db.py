import sqlite3
import os

def create_database():
    # Garante que a pasta data existe
    os.makedirs("data", exist_ok=True)
    db_path = "data/security_hub.db"
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Tabela de Usuários/Ativos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assets_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            department TEXT NOT NULL,
            role TEXT NOT NULL,
            risk_level TEXT DEFAULT 'Baixo'
        )
    """)
    
    # Tabela de Logs de Acesso e Autenticação (Eventos de Segurança)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS access_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            username TEXT NOT NULL,
            action TEXT NOT NULL, -- 'LOGIN_SUCCESS', 'LOGIN_FAILED', 'PASSWORD_RESET', 'PRIVILEGE_ESCALATION'
            status TEXT NOT NULL, -- 'SUCCESS', 'BLOCKED', 'SUSPICIOUS'
            location TEXT NOT NULL
        )
    """)
    
    # Tabela de Incidentes de Segurança (SOC)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS security_incidents (
            incident_id TEXT PRIMARY KEY,
            detected_at TEXT NOT NULL,
            incident_type TEXT NOT NULL, -- 'Brute Force', 'Unauthorized Access', 'Malware Alert'
            severity TEXT NOT NULL, -- 'Baixa', 'Média', 'Alta', 'Crítica'
            status TEXT NOT NULL, -- 'Aberto', 'Em Investigação', 'Resolvido'
            resolved_at TEXT,
            assigned_to TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    print("[INFO] Banco de dados SQLite 'security_hub.db' criado com sucesso na pasta data/!")

if __name__ == "__main__":
    create_database()