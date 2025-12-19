from src.dao.midia_dao import MidiaDAO
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
        choice = input("Selecione uma opção: ").strip()

        if choice == "0":
            Interface.exibir_mensagem_de_saida()
            break

        elif choice == "1":
            midias = MidiaDAO.listar_todos()
            Interface.exibir_catalogo(midias)

        elif choice == "2":
            try:
                nova_midia = Interface.solicitar_dados_midia()

                MidiaDAO.salvar(nova_midia)

                Interface.exibir_mensagem_sucesso(
                    f"'{nova_midia.titulo}' salvo no banco!"
                )
            except Exception as e:
                Interface.exibir_mensagem_erro(f"Falha ao salvar: {e}")

        elif choice == "3":
            try:
                id_del = int(input("ID para remover: "))
                if MidiaDAO.deletar(id_del):
                    Interface.exibir_mensagem_sucesso("Mídia removida.")
                else:
                    Interface.exibir_mensagem_erro("ID não encontrado.")
            except ValueError:
                Interface.exibir_mensagem_erro("Digite um número válido.")
        else:
            Interface.exibir_mensagem_opcao_invalida(choice)


if __name__ == "__main__":
    main()
