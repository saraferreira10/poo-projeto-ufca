

from src.models.midia import Midia
from typing import List, Optional


class Catalog():    
    def __init__(self) -> None:
        self._midias: List[Midia] = []
        self._proximo_id = 1
    
    # --- GETTER ---
    @property
    def midias(self) -> List[Midia]:
        return self._midias.copy()
    
    # --- MÉTODOS DE GERENCIAMENTO ---
    def adicionar_midia(self, midia: Midia) -> None:
        if not isinstance(midia, Midia):
            raise TypeError("Somente objetos do tipo Midia podem ser adicionados.")
        
        # Verifica se a mídia já existe no catálogo
        if midia in self._midias:
            raise ValueError(f"A mídia '{midia.titulo}' já existe no catálogo.")
        
        # Atribui um ID único à mídia
        midia.id = self._proximo_id
        self._proximo_id += 1
        
        self._midias.append(midia)
        print(f"Mídia '{midia.titulo}' adicionada ao catálogo.")
    
    def remover_midia(self, id_midia: int) -> None:
        midia = self.buscar_por_id(id_midia)
        if midia:
            self._midias.remove(midia)
            print(f"✓ Mídia '{midia.titulo}' removida do catálogo.")
        else:
            raise ValueError(f"Mídia com ID {id_midia} não encontrada no catálogo.")
    
    def buscar_por_id(self, id_midia: int) -> Optional[Midia]:
        for midia in self._midias:
            if midia.id == id_midia:
                return midia
        return None
    
    def buscar_por_titulo(self, titulo: str) -> List[Midia]:
        titulo_lower = titulo.lower()
        return [m for m in self._midias if titulo_lower in m.titulo.lower()]
    
    def buscar_por_tipo(self, tipo: str) -> List[Midia]:
        return [m for m in self._midias if m.tipo == tipo]
    
    def buscar_por_genero(self, genero: str) -> List[Midia]:
        return [m for m in self._midias if m.genero == genero]
    
    def buscar_por_ano(self, ano: int) -> List[Midia]:
        return [m for m in self._midias if m.ano == ano]
    
    def listar_todas(self) -> None:
        if not self._midias:
            print("Catálogo vazio.")
            return
        
        print(f"\n{'='*60}")
        print(f"CATÁLOGO DE MÍDIAS ({len(self._midias)} itens)")
        print(f"{'='*60}\n")
        
        for midia in self._midias:
            print(f"ID: {midia.id}")
            print(midia)
            print()
    
    def ordenar_por_nota(self) -> List[Midia]:
        return sorted(self._midias, key=lambda m: m.nota, reverse=True)
    
    def ordenar_por_titulo(self) -> List[Midia]:
        return sorted(self._midias, key=lambda m: m.titulo.lower())
    
    def obter_estatisticas(self) -> dict:
        if not self._midias:
            return {
                "total": 0,
                "nota_media": 0.0,
                "melhor_nota": 0.0,
                "pior_nota": 0.0
            }
        
        notas = [m.nota for m in self._midias if m.nota > 0]
        
        return {
            "total": len(self._midias),
            "nota_media": sum(notas) / len(notas) if notas else 0.0,
            "melhor_nota": max(notas) if notas else 0.0,
            "pior_nota": min(notas) if notas else 0.0
        }
    
    # --- MÉTODOS ESPECIAIS ---
    def __len__(self) -> int:
        return len(self._midias)
    
    def __str__(self) -> str:
        return f"Catálogo com {len(self._midias)} mídia(s)"
    
    def __repr__(self) -> str:
        return f"Catalog(midias={len(self._midias)})"

# TODO: Criar métodos calcular_media_por_genero, tempo_total_assistido
# top_10_avaliacoes
# series_mais_episodios_assistidos (Aguardando criação das Séries)
