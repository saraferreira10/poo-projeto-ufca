from src.enums.enums import Classificacao, Genero
from src.models.filme import Filme


def main():
    # criar_tabelas()

    try:
        print("--- Iniciando Cadastro de Mídia ---")

        m1 = Filme(
            titulo="Inception",
            genero=Genero.FICCAO_CIENTIFICA,
            ano=2010,
            duracao=148,
            classificacao=Classificacao.C14,
            elenco="Leo DiCaprio",
        )

        print(m1)
        m1.iniciar_visualizacao()
        m1.avaliar(9.5)
        print(m1)

    except ValueError as e:
        print(f"\n❌ ERRO DE VALIDAÇÃO: {e}")

    except Exception as e:
        print(f"\n❗ OCORREU UM ERRO: {e}")

    finally:
        print("\n--- Operação Finalizada ---")


if __name__ == "__main__":
    main()
