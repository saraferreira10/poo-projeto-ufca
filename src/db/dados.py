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
    # Tabela Usuário
    # ------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    )
    """)

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
        FOREIGN KEY(midia_id) REFERENCES midia(id) ON DELETE CASCADE,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
    )
    """)

    # ------------------------
    # Tabela Episodio Nota
    # ------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS episodio_notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        episodio_id INTEGER NOT NULL,
        usuario_id INTEGER NOT NULL,
        nota INTEGER NOT NULL,
        FOREIGN KEY(episodio_id) REFERENCES episodios(id) ON DELETE CASCADE,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
    )
    """)

    # ------------------------
    # Tabela Visualização de Episódio
    # ------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS visualizacoes_episodio (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        episodio_id INTEGER NOT NULL,
        usuario_id INTEGER NOT NULL,
        status TEXT NOT NULL,
        UNIQUE(episodio_id, usuario_id),
        FOREIGN KEY(episodio_id) REFERENCES episodios(id) ON DELETE CASCADE,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
    )
    """)
    
    # ------------------------
    # Tabela Visualização de Filme (Midia)
    # ------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS visualizacoes_filme (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        midia_id INTEGER NOT NULL,
        usuario_id INTEGER NOT NULL,
        status TEXT NOT NULL,
        data_visualizacao TEXT, 
        UNIQUE(midia_id, usuario_id),
        FOREIGN KEY(midia_id) REFERENCES midia(id) ON DELETE CASCADE,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso.")

if __name__ == "__main__":
    criar_tabelas()