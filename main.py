import sqlite3
from src.dao.midia_dao import MidiaDAO
from src.dao.avaliacao_dao import AvaliacaoDAO
from src.dao.usuario_dao import UsuarioDAO
from src.db.dados import criar_tabelas
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
            
            if sub == "adicionar-episodio":
                Interface.exibir_mensagem_de_todo()

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