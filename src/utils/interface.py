class Interface:
    LARGURA = 80
    LINHA_DUPLA = "=" * LARGURA
    LINHA_SIMPLES = "-" * LARGURA

    @staticmethod
    def exibir_menu_principal():
        menu = (
            f"\n{Interface.LINHA_DUPLA}\n"
            f"{'MENU PRINCIPAL'.center(Interface.LARGURA)}\n"
            f"{Interface.LINHA_DUPLA}\n"
            f" [1] Ver Catálogo\n"
            f" [0] Sair do Sistema\n"
            f"{Interface.LINHA_SIMPLES}"
        )
        print(menu)

    @staticmethod
    def exibir_mensagem_de_saida():
        mensagem = (
            f"\nEncerrando o sistema... \n"
            f"Sistema encerrado\n"
        )
        print(mensagem)

    @staticmethod
    def exibir_mensagem_opcao_invalida(opcao):
        mensagem = (
            f"{Interface.LINHA_SIMPLES}"
            f"\n'{opcao}' é uma opção inválida :(\n"
            f"\n                               Tente novamente :) \n"
            f"{Interface.LINHA_SIMPLES}"
        )
        print(mensagem)

    @staticmethod
    def exibir_mensagem_de_todo():
        mensagem = (
            f"{Interface.LINHA_SIMPLES}"
            f"\nImplementar função\n"
            f"{Interface.LINHA_SIMPLES}"
        )
        print(mensagem)