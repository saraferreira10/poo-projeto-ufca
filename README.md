<p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Bras%C3%A3o_UFCA_em_Alta_Defini%C3%A7%C3%A3o.svg" alt="Logo UFCA" width="200"> </p>

# 🎬 Projeto POO – CATÁLOGO DE FILMES E SÉRIES

## Sumário
- [Integrantes da Equipe](#integrantes-da-equipe)
- [Principais Classes do Projeto (UML Textual)](#principais-classes-do-projeto-uml-textual)
  - [Usuario](#usuario)
  - [Catalogo](#catalogo)
  - [ListaPersonalizada](#listapersonalizada)
  - [RegistroHistorico](#registrohistorico)
  - [Midia (abstrata)](#midia-abstrata)
  - [Filme](#filme)
  - [Serie](#serie)
  - [Temporada](#temporada)
  - [Episodio](#episodio)
- [Enums Utilizadas no Sistema](#enums-utilizadas-no-sistema)

## Integrantes da Equipe
- Carlos Anderson Dos Santos De Souza:
  * Modelagem e implementação de *Catalogo* e *ListaPersonalizada*  
  * Implementação de métodos simples de relatórios no catálogo (ex.: tempo total assistido, listar séries/favoritos)  

- Holivane Pessoa Holanda Cabrini:
  - Modelagem e implementação de *Usuario* e *RegistroHistorico*  
  - Implementação de métodos de avaliação, marcação de assistido e cálculo de médias  
  - Validações de dados  

- Sara Ferreira de Araújo:
  * Modelagem de classes principais: *Midia, Filme, Serie, Temporada, Episodio*  
  * Desenvolvimento da *API FastAPI / CLI*  
  * Integração com *persistência (SQLite/JSON)*

# Principais Classes do Projeto (UML Textual)

---

### **Usuario**
**Classe:** Usuario  

**Atributos:**  
- nome  
- email  
- catalogo  
- listas_personalizadas  
- historico  

**Métodos:**  
- adicionar_lista  
- remover_lista  
- adicionar_midia_a_lista  
- registrar_no_historico  
- obter_historico  
- obter_tempo_assistido  
- tempo_assistido_no_periodo  
- obter_listas  

---

### **Catalogo**
**Classe:** Catalogo  

**Atributos:**  
- midias  

**Métodos:**  
- adicionar_midia  
- remover_midia  
- buscar_midia_por_titulo  
- buscar_por_titulo  
- verificar_duplicidade  
- calcular_media_geral  
- calcular_media_por_genero  
- tempo_total_assistido  
- top_10_avaliacoes  
- series_mais_episodios_assistidos  

---

### **ListaPersonalizada**
**Classe:** ListaPersonalizada  

**Atributos:**  
- nome  
- midias  

**Métodos:**  
- adicionar_midia  
- remover_midia  
- listar_midias  

---

### **RegistroHistorico**
**Classe:** RegistroHistorico  

**Atributos:**  
- midia  
- data_conclusao  
- duracao_consumida  

**Métodos:**  
*(apenas armazenamento de dados)*  

---

### **Midia** *(abstrata)*
**Classe:** Midia

**Atributos:**  
- titulo  
- tipo — definido nas subclasses (FILME ou SERIE)  
- genero  
- ano  
- duracao  
- classificacao  
- elenco  
- status  
- concluido_em  
- nota  

**Métodos:**  
- avaliar  
- marcar_assistido  
- calcular_media  

**Observações sobre polimorfismo:**  
A classe **Midia** define a interface comum para qualquer tipo de conteúdo do catálogo.  
Os métodos `avaliar`, `marcar_assistido` e `calcular_media` são **sobrescritos pelas subclasses** para comportamentos distintos.  

---

### **Filme**
**Classe:** Filme *(herda de Midia)*

**Atributos:**  
- tipo — sempre `TipoMidia.FILME`  

**Métodos:**  
*(herda os métodos de Midia)*  

**Observações sobre polimorfismo:**  
- Avaliação é direta e única para o filme.  
- Marcar como assistido é imediato.  
- Duração é fixa e não depende de episódios.  
- Filme usa a implementação padrão da classe abstrata Midia.

---

### **Serie**
**Classe:** Serie *(herda de Midia)*

**Atributos:**  
- tipo — sempre `TipoMidia.SERIE`  
- temporadas  

**Métodos:**  
- adicionar_temporada  
- adicionar_episodio  
- avaliar  
- marcar_assistido  
- calcular_media  
- atualizar_duracao  

**Observações sobre polimorfismo:**  
- Avaliação é feita por episódio.  
- Marcar como assistido só ocorre quando todos os episódios estão concluídos.  
- Calcular média soma notas dos episódios.  
- Duração é a soma de todos os episódios.  
- Serie sobrescreve os métodos herdados de Midia para comportamento específico de série.

---

### **Temporada**
**Classe:** Temporada  

**Atributos:**  
- numero  
- episodios  

**Métodos:**  
- adicionar_episodio  
- obter_episodio  
- episodios_assistidos  
- total_episodios  

---

### **Episodio**
**Classe:** Episodio  

**Atributos:**  
- numero  
- titulo  
- duracao  
- data_lancamento  
- status  
- nota  
- concluido_em  

**Métodos:**  
- avaliar  
- marcar_assistido  

---

# Enums Utilizadas no Sistema

### **Enum: TipoMidia**
- FILME  
- SERIE  

### **Enum: StatusVisualizacao**
- NAO_ASSISTIDO  
- ASSISTINDO  
- ASSISTIDO  

### **Enum: Genero**
- ACAO  
- AVENTURA  
- COMEDIA  
- COMEDIA_ROMANTICA  
- DRAMA  
- FICCAO_CIENTIFICA  
- TERROR  
- SUSPENSE  
- ROMANCE  
- FANTASIA  
- MUSICAL  
- DOCUMENTARIO  
- BIOGRAFIA  
- ANIMACAO  
- GUERRA  
- HISTORICO  
- POLICIAL  

### **Enum: Classificacao**
- L  
- 10  
- 12  
- 14  
- 16  
- 18  


