import sqlite3
from src.dao.episodio_dao import EpisodioDAO
from src.dao.midia_dao import MidiaDAO
from src.dao.avaliacao_dao import AvaliacaoDAO
from src.dao.temporada_dao import TemporadaDAO
from src.dao.usuario_dao import UsuarioDAO
from src.db.dados import criar_tabelas
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
                    midia_id = int(input("ID da mídia para avaliar: "))
                    avaliacao = Interface.solicitar_dados_avaliacao(midia_id, user_logado.id)
                    if avaliacao:
                        AvaliacaoDAO.salvar_avaliacao(avaliacao)
                        Interface.exibir_mensagem_sucesso("Avaliação registrada!")
                except Exception as e: Interface.exibir_mensagem_erro(e)

            elif sub == "relatorio top":
                Interface.exibir_mensagem_de_todo()

        # --- SUBCOMANDOS: SERIE ---
        elif entrada.startswith("serie "):
            sub = entrada.replace("serie ", "")
            
            if entrada == "serie adicionar-episodio":
                try:
                    series = [m for m in MidiaDAO.listar_todos() if m.tipo.upper() == "SERIE"]
                    if not series:
                        Interface.exibir_mensagem_erro("Nenhuma série cadastrada.")
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
                Interface.exibir_mensagem_de_todo()

        # --- SUBCOMANDOS: USUARIO ---
        elif entrada.startswith("usuario "):
            sub = entrada.replace("usuario ", "")

            if sub == "criar-lista":
                nome_lista = input("Nome da lista personalizada: ")
                Interface.exibir_mensagem_sucesso(f"Lista '{nome_lista}' criada para {user_logado.name}")

            elif sub == "adicionar-favorito":
                Interface.exibir_mensagem_de_todo()

        else:
            Interface.exibir_mensagem_opcao_invalida(entrada)

if __name__ == "__main__":
    main()