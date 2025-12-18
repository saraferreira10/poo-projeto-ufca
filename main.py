



from src.db.dados import criar_tabelas



def main():
    print("🎬 Sistema de Catálogo de Mídias - CLI Iniciado")
    
    criar_tabelas()  # Inicializa o banco/SQLITE
    
    print("✅ Sistema inicializado com sucesso!\n")

if __name__ == "__main__":
    main()