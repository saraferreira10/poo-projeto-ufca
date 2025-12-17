from src.enums.enums import Classificacao, Genero, TipoMidia
from src.models.midia import Midia

def main():
    # criar_tabelas() 
    
    try:
        print("--- Iniciando Cadastro de Mídia ---")
        
        M1 = Midia(
            titulo="tal", 
            tipo=TipoMidia.FILME, 
            genero=Genero.AVENTURA, 
            ano=2012, 
            duracao=120, 
            classificacao=Classificacao.C10, 
            elenco="1, 2, 4"
        )

        M2 = Midia(
            titulo="tal", 
            tipo=TipoMidia.FILME, 
            genero=Genero.AVENTURA, 
            ano=2012, 
            duracao=120, 
            classificacao=Classificacao.C10, 
            elenco="1, 2, 4"
        )
        
        # print(f"Título: {M1.titulo}")
        # M1.titulo = "ATUALIZADO"
        # print(f"Título Atualizado: {M1.titulo}")
        # print(f"Gênero: {M1.genero}")
        # print(f"Classificação: {M1.classificacao}")
        print(M1 == M2)

    except ValueError as e:
        print(f"\n❌ ERRO DE VALIDAÇÃO: {e}")

    except Exception as e:
        print(f"\n❗ OCORREU UM ERRO: {e}")

    finally:
        print("\n--- Operação Finalizada ---")

if __name__ == "__main__":
    main()