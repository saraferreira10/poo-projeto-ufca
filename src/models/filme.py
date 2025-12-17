from datetime import datetime
from src.enums.enums import StatusVisualizacao, TipoMidia
from src.models.midia import Midia


# --- FILME ---
class Filme(Midia):
    # ---  MÉTODO CONSTRUTOR ---
    def __init__(self, titulo, genero, ano, duracao, classificacao, elenco):
        super().__init__(
            titulo, TipoMidia.FILME, genero, ano, duracao, classificacao, elenco
        )

    # --- IMPLEMENTAÇÃO DOS MÉTODOS ABSTRATOS ---
    def marcar_assistido(self) -> None:
        self._status = StatusVisualizacao.ASSISTIDO
        self._concluido_em = datetime.now()
        print(
            f"O filme '{self.titulo}' foi marcado como assistido em {self._concluido_em.strftime('%d/%m/%Y')}."
        )

    def avaliar(self, nota: float) -> None:
        if not (0 <= nota <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")

        self._nota = float(nota)
        print(f"Filme '{self.titulo}' avaliado com nota {self._nota}.")

    def calcular_media(self) -> float:
        return self.nota

    # DEMAIS MÉTODOS
    def iniciar_visualizacao(self) -> None:
        self._status = StatusVisualizacao.ASSISTINDO
        print(f"Começou a ver: {self.titulo}")

