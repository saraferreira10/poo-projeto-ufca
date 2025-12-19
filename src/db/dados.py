import sqlite3

DB_FILE = "catalogo.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    # ------------------------
    # Tabela Mídia
    # ------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS midia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL,    
        titulo TEXT NOT NULL,
        genero TEXT NOT NULL,
        ano INTEGER NOT NULL,
        classificacao TEXT NOT NULL,
        elenco TEXT,
        duracao INTEGER DEFAULT 0
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
        FOREIGN KEY(temporada_id) REFERENCES temporadas(id) ON DELETE CASCADE
    )
    """)

    # ------------------------
    # Tabela Avaliação
    # ------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS avaliacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        midia_id INTEGER NOT NULL,
        nota INTEGER NOT NULL,
        comentario TEXT,
        data_avaliacao TEXT NOT NULL,
        FOREIGN KEY(midia_id) REFERENCES midia(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso.")