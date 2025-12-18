from src.db.dados import criar_tabelas


def main():
    print("Sistema de Catálogo de Mídias - CLI Iniciado")
    print("Inicializando banco de dados...\n")
    
    criar_tabelas()  # Inicializa o banco/SQLITE
    print("✅ Banco de dados SQLite inicializado com sucesso!")
    print("✅ Sistema inicializado com sucesso!\n")

    while True:
        print("\n=== MENU === \n")
        print("-> Digite 'Sair' para encerrar o sistema ") 

        choice = input().strip().lower()

        if choice == "0" or choice == "sair":
            print("\nEncerrando o sistema... \nSistema encerrado \n \n")
            break
        else:
            print("!!! Opção inválida :( \n Tente novamente")


if __name__ == "__main__":
    main()