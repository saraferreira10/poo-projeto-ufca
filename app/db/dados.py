import sqlite3

DB_FILE = "catalogo.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS midia (
        id TEXT PRIMARY KEY,
        tipo TEXT NOT NULL,
        titulo TEXT NOT NULL,
        genero TEXT,
        status TEXT,
        elenco TEXT,
        classificacao TEXT,
        nota INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmes (
        id TEXT PRIMARY KEY,
        duracao INTEGER NOT NULL,
        FOREIGN KEY(id) REFERENCES midia(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()
