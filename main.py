import sqlite3
from src.dao.episodio_dao import EpisodioDAO
from src.dao.episodio_nota_dao import EpisodioNotaDAO
from src.dao.midia_dao import MidiaDAO
from src.dao.avaliacao_dao import AvaliacaoDAO
from src.dao.temporada_dao import TemporadaDAO
from src.dao.usuario_dao import UsuarioDAO
from src.dao.visualizacao_dao import VisualizacaoDAO
from src.db.dados import criar_tabelas
from src.models.avaliacao import Avaliacao
from src.models.episodio import Episodio
from src.models.temporada import Temporada
from src.models.user import User
from src.utils.interface import Interface

def inicializar_usuario_padrao():
    """Garante que existe pelo menos um usuário no sistema para as operações."""
    usuario = UsuarioDAO.buscar_por_id(1)
    if not usuario:
        usuario_novo = User(name="Usuario Padrao", email="padrao@catalogo.com")
        UsuarioDAO.salvar(usuario_novo)
        return usuario_novo
    return usuario

def main():
    print("Sistema de Catálogo de Mídias - CLI Iniciado")
    criar_tabelas()
    
    # Inicializa ou recupera o usuário padrão (ID 1)
    user_logado = inicializar_usuario_padrao()
    
    print(f"✅ Sistema inicializado! Logado como: {user_logado.name} (ID: {user_logado.id})")

    while True:
        Interface.exibir_ajuda_comandos() 
        entrada = input("\n$ ").strip().lower()

        if not entrada:
            continue

        if entrada == "sair" or entrada == "0":
            Interface.exibir_mensagem_de_saida()
            break

        # --- SUBCOMANDOS: MIDIA ---
        elif entrada.startswith("midia "):
            sub = entrada.replace("midia ", "")
            
            if sub == "listar":
                midias = MidiaDAO.listar_todos()
                Interface.exibir_catalogo(midias)
            
            elif sub == "adicionar":
                try:
                    nova_midia = Interface.solicitar_dados_midia()
                    MidiaDAO.salvar(nova_midia)
                    Interface.exibir_mensagem_sucesso(f"'{nova_midia.titulo}' adicionado.")
                except sqlite3.IntegrityError:
                    Interface.exibir_mensagem_erro(
                        f"A mídia '{nova_midia.titulo}' ({nova_midia.ano}) já está cadastrada!"
                    )
                except Exception as e: 
                    Interface.exibir_mensagem_erro(f"Falha ao salvar: {e}")
                    
            elif sub == "avaliar":
                try:
                    midias = MidiaDAO.listar_todos()
                    Interface.exibir_catalogo(midias)
                    
                    midia_id = int(input("\nID da mídia que deseja avaliar: "))
                    selecionada = next((m for m in midias if m["id"] == midia_id), None)

                    if not selecionada:
                        Interface.exibir_mensagem_erro("Mídia não encontrada.")
                        continue

                    user_id = int(input("Informe seu ID de Usuário: "))

                    if selecionada["tipo"].upper() == "SERIE":
                        episodios = EpisodioDAO.buscar_por_midia_id(midia_id) 

                        if not episodios:
                            Interface.exibir_mensagem_erro("Esta série não tem episódios.")
                            continue

                        print("\n--- EPISÓDIOS DISPONÍVEIS ---")
                        for ep in episodios:
                            print(f" ID: {str(ep.id).ljust(3)} | Ep {ep.numero}: {ep.titulo}")
                        
                        ep_id = int(input("\nID do Episódio: "))
                        nota = int(input("Nota (1-10): "))

                        EpisodioNotaDAO.salvar(ep_id, user_id, nota)
                        Interface.exibir_mensagem_sucesso("Nota do episódio registrada!")

                    else:
                        nota = int(input(f"Nota para o filme '{selecionada['titulo']}' (1-10): "))
                        comentario = input("Comentário (opcional): ")
                        
                        nova_avaliacao = Avaliacao(
                            usuario_id=user_id, 
                            midia_id=midia_id, 
                            nota=nota, 
                            comentario=comentario
                        )
                        
                        AvaliacaoDAO.salvar_avaliacao(nova_avaliacao)
                        
                        Interface.exibir_mensagem_sucesso("Avaliação do filme registrada!")

                except ValueError:
                    Interface.exibir_mensagem_erro("Por favor, insira apenas números.")
                except Exception as e:
                    Interface.exibir_mensagem_erro(f"Erro ao avaliar: {e}")
            elif sub == "relatorio top":
                Interface.exibir_mensagem_de_todo()

        # --- SUBCOMANDOS: SERIE ---
        elif entrada.startswith("serie "):
            sub = entrada.replace("serie ", "")
            
            if sub == "adicionar-episodio":
                try:
                    todas_midias = MidiaDAO.listar_todos()
                    series = [m for m in todas_midias if m["tipo"].upper() == "SERIE"]
                    
                    if not series:
                        Interface.exibir_mensagem_erro("Nenhuma série cadastrada no sistema.")
                        continue

                    Interface.exibir_catalogo(series)
                    
                    midia_id = int(input("\nID da Série: "))
                    
                    num_temporada = int(input("Número da Temporada (ex: 1): "))
                    
                    
                    temporadas_da_serie = TemporadaDAO.buscar_por_midia_id(midia_id)
                    
                    temp_obj = next((t for t in temporadas_da_serie if t.numero == num_temporada), None)

                    if temp_obj is None:
                        print(f"⚙️ Temporada {num_temporada} não encontrada. Criando...")
                        nova_temp = Temporada(numero=num_temporada)
                        TemporadaDAO.salvar(nova_temp, midia_id)
                        temp_id = nova_temp.id
                    else:
                        temp_id = temp_obj.id

                    dados_ep = Interface.solicitar_dados_episodio()
                    
                    
                    novo_episodio = Episodio(
                        numero=dados_ep['numero'],
                        titulo=dados_ep['titulo'],
                        duracao=dados_ep['duracao']
                    )
                    
                    EpisodioDAO.salvar(novo_episodio, temporada_id=temp_id)
                    
                    Interface.exibir_mensagem_sucesso(f"Episódio '{dados_ep['titulo']}' salvo com sucesso!")

                except Exception as e:
                    Interface.exibir_mensagem_erro(f"Erro ao processar: {e}")
            elif sub == "atualizar-status":
                try:
                    midias = MidiaDAO.listar_todos()
                    series = [m for m in midias if m["tipo"].upper() == "SERIE"]
                    Interface.exibir_catalogo(series)
                    
                    midia_id = int(input("\nID da série: "))
                    
                    episodios = EpisodioDAO.buscar_por_midia_id(midia_id)
                    
                    if not episodios:
                        Interface.exibir_mensagem_erro("Série sem episódios cadastrados.")
                        continue

                    print(f"\n{' EPISÓDIOS DISPONÍVEIS '.center(40, '-')}")
                    for ep in episodios:
                        print(f" ID: {str(ep.id).ljust(3)} | Ep {ep.numero}: {ep.titulo}")

                    ep_id = int(input("\nID do episódio: "))
                    user_id = int(input("Informe seu ID de usuário: "))
                    
                    print("\nQual o novo status?")
                    print("[1] NÃO ASSISTIDO")
                    print("[2] ASSISTINDO")
                    print("[3] ASSISTIDO")
                    opcao = input("Escolha (1-3): ")

                    mapeamento = {
                        "1": "NÃO ASSISTIDO",
                        "2": "ASSISTINDO",
                        "3": "ASSISTIDO"
                    }

                    novo_status = mapeamento.get(opcao)
                    if not novo_status:
                        Interface.exibir_mensagem_erro("Opção inválida.")
                        continue

                    if VisualizacaoDAO.atualizar_status(ep_id, user_id, novo_status):
                        Interface.exibir_mensagem_sucesso(f"Episódio {ep_id} agora está como: {novo_status}")

                except ValueError:
                    Interface.exibir_mensagem_erro("Entrada inválida. Digite apenas números.")
                except Exception as e:
                    Interface.exibir_mensagem_erro(f"Erro inesperado: {e}")

        # --- SUBCOMANDOS: USUARIO ---
        elif entrada.startswith("usuario "):
            sub = entrada.replace("usuario ", "")

            if sub == "criar-lista":
                Interface.exibir_mensagem_de_todo()

            elif sub == "adicionar-favorito":
                Interface.exibir_mensagem_de_todo()

        elif entrada == "filme atualizar-status":
            try:
                midias = MidiaDAO.listar_todos()
                filmes = [m for m in midias if m["tipo"].upper() == "FILME"]
                
                if not filmes:
                    Interface.exibir_mensagem_erro("Nenhum filme cadastrado no catálogo.")
                    continue
                
                Interface.exibir_catalogo(filmes)
                
                midia_id = int(input("\nID do filme para atualizar status: "))
                
                selecionado = next((f for f in filmes if f["id"] == midia_id), None)
                if not selecionado:
                    Interface.exibir_mensagem_erro("Filme não encontrado ou o ID informado não é um filme.")
                    continue

                user_id = int(input("Informe seu ID de usuário: "))
                
                print(f"\n--- ATUALIZAR STATUS: {selecionado['titulo']} ---")
                print("[1] NÃO ASSISTIDO")
                print("[2] ASSISTINDO")
                print("[3] ASSISTIDO")
                opcao = input("Escolha uma opção (1-3): ")

                mapeamento = {
                    "1": "NÃO ASSISTIDO",
                    "2": "ASSISTINDO",
                    "3": "ASSISTIDO"
                }

                novo_status = mapeamento.get(opcao)
                if not novo_status:
                    Interface.exibir_mensagem_erro("Opção inválida.")
                    continue

                from src.dao.visualizacao_filme_dao import VisualizacaoFilmeDAO
                if VisualizacaoFilmeDAO.atualizar_status(midia_id, user_id, novo_status):
                    Interface.exibir_mensagem_sucesso(f"Filme '{selecionado['titulo']}' atualizado para: {novo_status}")

            except ValueError:
                Interface.exibir_mensagem_erro("Entrada inválida. Use apenas números para IDs e opções.")
            except Exception as e:
                Interface.exibir_mensagem_erro(f"Erro ao processar atualização: {e}")
        else:
            Interface.exibir_mensagem_opcao_invalida(entrada)

if __name__ == "__main__":
    main()