from src.enums.enums import Genero


from src.enums.enums import TipoMidia, Genero, Classificacao
from src.models.filme import Filme
from src.models.serie import Serie


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
            f" [2] Adicionar Mídia\n"
            f" [3] Remover Mídia\n"
            f" [0] Sair do Sistema\n"
            f"{Interface.LINHA_SIMPLES}"
        )
        print(menu)

    @staticmethod
    def exibir_catalogo(midias):
        print(f"\n{Interface.LINHA_DUPLA}")
        print(f"{'CATÁLOGO DE MÍDIAS'.center(Interface.LARGURA)}")
        print(f"{Interface.LINHA_DUPLA}")

        if not midias:
            print(f"\n{'O catálogo está vazio.'.center(Interface.LARGURA)}\n")
        else:
            for m in midias:
                id_str = str(m.id) if m.id is not None else "N/A"
                print(f" ID: {id_str.ljust(3)} | {m}")

        print(f"{Interface.LINHA_SIMPLES}")

    @staticmethod
    def solicitar_dados_midia():
        print(f"\n{Interface.LINHA_SIMPLES}")
        print(f"{' NOVO CADASTRO '.center(Interface.LARGURA, '#')}")
        print(f"{Interface.LINHA_SIMPLES}")

        titulo = input("Título: ").strip()

        print(f"\nTipo: [1] Filme | [2] Série")
        t_op = input("Opção: ").strip()
        tipo = TipoMidia.SERIE if t_op == "2" else TipoMidia.FILME

        # --- CONVERSÃO DE GÊNERO ---
        print(f"\nGêneros Disponíveis:")
        for g in Genero:
            print(f" - {g.value}")

        genero_input = input("Digite o gênero (ex: Comédia): ").strip()
        genero = next((g for g in Genero if g.value == genero_input), None)

        if not genero:
            raise ValueError(f"Gênero '{genero_input}' não reconhecido.")

        ano = int(input("Ano de Lançamento: "))

        print(f"\nClassificações: L, 10, 12, 14, 16, 18")
        class_input = input("Digite a classificação: ").strip()
        classificacao = next((c for c in Classificacao if c.value == class_input), None)

        if not classificacao:
            raise ValueError(f"Classificação '{class_input}' não reconhecida.")

        elenco = input("Elenco (atores separados por vírgula): ").strip()

        if tipo == TipoMidia.FILME:
            duracao = int(input("Duração em minutos: "))
            return Filme(
                titulo=titulo,
                genero=genero,
                ano=ano,
                classificacao=classificacao,
                elenco=elenco,
                duracao=duracao,
            )
        else:
            return Serie(
                titulo=titulo,
                genero=genero,
                ano=ano,
                classificacao=classificacao,
                elenco=elenco,
            )

    @staticmethod
    def exibir_mensagem_sucesso(texto):
        print(f"\n✅ SUCESSO: {texto}")

    @staticmethod
    def exibir_mensagem_erro(texto):
        print(f"\n❌ ERRO: {texto}")

    @staticmethod
    def exibir_mensagem_de_saida():
        mensagem = f"\nEncerrando o sistema... \n" f"Sistema encerrado\n"
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
