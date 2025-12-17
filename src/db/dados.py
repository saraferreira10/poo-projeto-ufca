import sqlite3

DB_FILE = "catalogo.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    # ------------------------
    # Tabela Midia
    # ------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS midia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL,
        titulo TEXT NOT NULL,
        genero TEXT,
        ano INTEGER,
        duracao INTEGER,
        classificacao TEXT,
        elenco TEXT,
        status TEXT,
        concluido_em TEXT,
        nota INTEGER DEFAULT 0
    )
    """)

    # ------------------------
    # Tabela Temporada
    # ------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS temporadas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        midia_id INTEGER NOT NULL,
        numero INTEGER NOT NULL,
        FOREIGN KEY(midia_id) REFERENCES midia(id) ON DELETE CASCADE
    )
    """)

    # ------------------------
    # Tabela Episodio
    # ------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS episodios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temporada_id INTEGER NOT NULL,
        numero INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        duracao INTEGER NOT NULL,
        data_lancamento TEXT,
        status TEXT,
        nota INTEGER DEFAULT 0,
        concluido_em TEXT,
        FOREIGN KEY(temporada_id) REFERENCES temporadas(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()