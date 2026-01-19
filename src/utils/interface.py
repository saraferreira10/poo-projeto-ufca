from src.dao.midia_dao import MidiaDAO
from src.enums.enums import Genero


from src.enums.enums import TipoMidia, Genero, Classificacao
from src.models.avaliacao import Avaliacao
from src.models.filme import Filme
from src.models.serie import Serie


class Interface:
    LARGURA = 120
    LINHA_DUPLA = "=" * LARGURA
    LINHA_SIMPLES = "-" * LARGURA

    # TELAS
    @staticmethod
    def exibir_tela_boas_vindas(usuario, estatisticas):
        print(f"\n{Interface.LINHA_DUPLA}")
        print(f"{' 🎬 CATÁLOGO DE MÍDIAS '.center(Interface.LARGURA, '*')}")
        print(f"{Interface.LINHA_DUPLA}")
        print(f"👤 Usuário: {usuario.nome} (ID: {usuario.id})")
        
        total = estatisticas.get('total', 0)
        filmes = estatisticas.get('filmes', 0)
        series = estatisticas.get('series', 0)
        tempo = estatisticas.get('tempo_total', 0)
        horas = tempo // 60
        
        print(f"📊 Resumo: {total} mídias | {filmes} filmes | {series} séries | ~{horas}h assistidas")

    @staticmethod
    def exibir_catalogo(midias):
        print(f"\n{'=' * Interface.LARGURA}")
        print(f"{'CATÁLOGO DE MÍDIAS'.center(Interface.LARGURA)}")
        print(f"{'=' * Interface.LARGURA}")

        if not midias:
            print(f"{'Nenhum item no catálogo.'.center(Interface.LARGURA)}")
        else:
            for m in midias:
                id_str = str(m["id"]).ljust(3)
                tipo = m["tipo"].upper()
                
                nota_val = m["media_nota"]
                nota_str = f"⭐ {nota_val:.1f}" if nota_val > 0 else "  N/A "

                linha = f" ID: {id_str} | [{tipo:^7}] {m['titulo'].ljust(20)} | {nota_str} | {m['genero'].ljust(12)}"
                
                if tipo == "SERIE":
                    linha += f" | {m['total_temps']} Temps | {m['total_eps']} Eps | {m['duracao_total_eps']} min"
                else:
                    linha += f" | {m['duracao']} min"
                
                print(linha)

        print(f"{'-' * Interface.LARGURA}\n")


    @staticmethod
    def exibir_usuarios(usuarios):
        print(f"\n{'=' * Interface.LARGURA}")
        print(f"{'USUÁRIOS CADASTRADOS'.center(Interface.LARGURA)}")
        print(f"{'=' * Interface.LARGURA}")

        if not usuarios:
            print(f"{'Nenhum usuário cadastrado.'.center(Interface.LARGURA)}")
        else:
            for u in usuarios:
                print(f" ID: {str(u.id).ljust(3)} | Nome: {u.nome.ljust(25)} | Email: {u.email}")

        print(f"{'-' * Interface.LARGURA}\n")


    @staticmethod
    def exibir_menu_compacto(usuario):
        print(f"\n{Interface.LINHA_SIMPLES}")
        print(f"USUÁRIO LOGADO: {usuario.nome} (ID: {usuario.id})")
        print(f"\n💡 Digite um comando ou 'help' para ver os comandos disponíveis")
        print(f"sair - Encerra o sistema")
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

    # CLI COM SUBCOMANDOS
    @staticmethod
    def exibir_comandos():
        print(f"\n{Interface.LINHA_DUPLA}")
        print(f"{'COMANDOS DISPONÍVEIS'.center(Interface.LARGURA)}")
        print(f"{Interface.LINHA_DUPLA}")
        
        # MÍDIA
        print(f"\n{'📚 MÍDIA'.ljust(20)}")
        print("  > midia listar               - Lista todas as mídias do catálogo")
        print("  > midia adicionar            - Adiciona uma nova mídia (filme ou série)")
        print("  > midia avaliar              - Avalia uma mídia do catálogo")
        print("  > midia relatorio top        - Exibe relatórios e top 10 do catálogo")
        
        # SÉRIE
        print(f"\n{'📺 SÉRIE'.ljust(20)}")
        print("  > serie adicionar-episodio   - Adiciona episódio a uma temporada")
        print("  > serie atualizar-status     - Atualiza status de visualização de episódio")
        
        # FILME
        print(f"\n{'🎬 FILME'.ljust(20)}")
        print("  > filme atualizar-status     - Atualiza status de visualização de filme")
        
        # USUÁRIO
        print(f"\n{'👤 USUÁRIO'.ljust(20)}")
        print("  > usuario listar             - Lista todos os usuários cadastrados")
        print("  > usuario criar-lista        - Cria uma lista personalizada")
        print("  > usuario adicionar-favorito - Adiciona mídia aos favoritos")
        
        # SISTEMA
        print(f"\n{'⚙️  SISTEMA'.ljust(20)}")
        print("  > sistema popular-banco      - Popula o banco com dados de exemplo")
        print("  > sistema resetar-banco      - Limpa todo o banco de dados")
        print("  > help / ajuda               - Exibe esta lista de comandos")
        print("  > sair                       - Encerra o sistema")
        
        print(f"{Interface.LINHA_SIMPLES}")

    @staticmethod
    def solicitar_dados_avaliacao(midia_id: int, usuario_id: int):
        """Coleta nota e comentário para avaliar uma mídia."""
        print(f"\n{Interface.LINHA_SIMPLES}")
        print(f"{' AVALIAR MÍDIA '.center(Interface.LARGURA, '*')}")
        
        try:
            nota_input = input("Nota (0 a 10): ").strip()
            if not nota_input:
                raise ValueError("A nota é obrigatória.")
            
            nota = int(nota_input)
            if not (0 <= nota <= 10):
                raise ValueError("A nota deve ser entre 0 e 10.")
            
            comentario = input("Comentário (opcional): ").strip()
                        
            return Avaliacao(
                usuario_id=usuario_id,
                midia_id=midia_id,
                nota=nota,
                comentario=comentario
            )
        except ValueError as e:
            Interface.exibir_mensagem_erro(f"Entrada inválida: {e}")
            return None

    
    @staticmethod
    def solicitar_dados_episodio():
        """Coleta dados para um novo episódio."""
        print(f"\n{Interface.LINHA_SIMPLES}")
        print(f"{' NOVO EPISÓDIO '.center(Interface.LARGURA, '*')}")
        try:
            numero = int(input("Número do Episódio: "))
            titulo = input("Título do Episódio: ").strip()
            duracao = int(input("Duração (minutos): "))
            
            return {
                "numero": numero,
                "titulo": titulo,
                "duracao": duracao
            }
        except ValueError:
            raise ValueError("Número e duração devem ser valores inteiros.")

    @staticmethod
    def exibir_relatorio_geral(medias_genero, tempos_tipo, series_top, ranking_top):
        print(f"\n{'#'*60}")
        print(f"{'📊 RELATÓRIOS DE CONSUMO E DESEMPENHO'.center(60)}")
        print(f"{'#'*60}")

        print(f"\n[ TEMPO TOTAL ASSISTIDO ]")
        for t in tempos_tipo:
            horas = t['total'] // 60
            print(f"- {t['tipo']}: {t['total']} min (~{horas}h)")

        print(f"\n[ MÉDIA DE NOTAS POR GÊNERO ]")
        for g in medias_genero:
            print(f"- {g['genero'].ljust(15)}: ⭐ {g['media']:.1f}")

        print(f"\n[ SÉRIES MAIS ASSISTIDAS (EPS) ]")
        for s in series_top:
            print(f"- {s['titulo'].ljust(20)}: {s['total_eps']} episódios")

        print(f"\n[ TOP 10 MÍDIAS DO CATÁLOGO ]")
        for i, m in enumerate(ranking_top, 1):
            print(f"{i}º {m['titulo'][:20].ljust(20)} | ⭐ {m['media']:.1f}")
        
        print(f"\n{'='*60}")
