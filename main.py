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
            Interface.exibir_mensagem_de_saida()
            break
        elif choice == "1":
            Interface.exibir_mensagem_de_todo()
        else:
            print("!!! Opção inválida :( \n Tente novamente")
            Interface.exibir_mensagem_opcao_invalida(choice)


if __name__ == "__main__":
    main()