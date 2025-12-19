from src.db.dados import criar_tabelas
from src.utils.interface import Interface


def main():
    print("Sistema de Catálogo de Mídias - CLI Iniciado")
    print("Inicializando banco de dados...\n")
    
    criar_tabelas()  # Inicializa o banco/SQLITE
    print("✅ Banco de dados SQLite inicializado com sucesso!")
    print("✅ Sistema inicializado com sucesso!\n")

    while True:
        Interface.exibir_menu_principal()

        choice = input("\n").strip().lower()

        if choice == "0":
            print("\nEncerrando o sistema... \nSistema encerrado \n \n")
            break
        elif choice == "1":
            print("-" * 80) 
            print("Chamar a função que lista o que está cadastrado no catálogo") 
            print("-" * 80) 
        else:
            print("!!! Opção inválida :( \n Tente novamente")


if __name__ == "__main__":
    main()