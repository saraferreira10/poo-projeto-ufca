from src.db.dados import criar_tabelas


def main():
    print("Sistema de Catálogo de Mídias - CLI Iniciado")
    print("Inicializando banco de dados...\n")
    
    criar_tabelas()  # Inicializa o banco/SQLITE
    print("✅ Banco de dados SQLite inicializado com sucesso!")
    print("✅ Sistema inicializado com sucesso!\n")

if __name__ == "__main__":
    main()