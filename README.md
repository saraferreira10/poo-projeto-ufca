<p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Bras%C3%A3o_UFCA_em_Alta_Defini%C3%A7%C3%A3o.svg" alt="Logo UFCA" width="200"> </p>

# 🎬 Projeto POO – CATÁLOGO DE FILMES E SÉRIES - (TEMA 10)
Sistema de **API mínima** para gerenciar um **Catálogo pessoal de filmes e séries**, com:
- Avaliações,
- Status de visualização,
- Temporadas/episódios,
- Histórico e
- Relatórios de consumo de mídia.

O sistema permite acompanhar o progresso de séries e comparar avaliações entre mídias. 

Persistência simples em SQLite
Modelagem orientada a objetos (herança, encapsulamento, validações e composição).

### Integrantes da Equipe
- Carlos Anderson Dos Santos De Souza

- Holivane Pessoa Holanda Cabrini:
  * Desenvolvimento da *CLI*
  * Documentação
  * Implementação de métodos de avaliação, marcação de assistido e cálculo de médias  
  * Implementação de métodos simples de relatórios no catálogo (ex.: tempo total assistido, listar séries/favoritos)
  * Modelagem e implementação de *Usuario*, *Catalogo*, *ListaPersonalizada* e *RegistroHistorico*  
  * Validações de dados  

- Sara Ferreira de Araújo:
  * Desenvolvimento da *CLI* 
  * Documentação
  * Integração com *persistência SQLite*
  * Implementação de métodos simples de relatórios no catálogo (ex.: tempo total assistido, listar séries/favoritos)
  * Modelagem de classes principais: *Midia, Filme, Serie, Temporada, Episodio* 
  * Organização do projeto e divisão das tarefas 

### Diagrama (em construção)
<details>
  <summary>Clique aqui para visualizar o diagrama</summary>

  ![Diagrama de Arquitetura](https://lucid.app/publicSegments/view/487020b6-9370-4baf-a7c8-294ae606d3b7/image.png)

</details>

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

## Principais Classes do Projeto (UML Textual)

### **Usuario**
**Classe:** Usuario (mapeada em `src/models/usuario.py`)

**Atributos:**  
- nome  
- email  
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

## Enums Utilizadas no Sistema

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

## 📺 Telas e Interface do Sistema

O sistema utiliza uma interface CLI (Command Line Interface) com comandos organizados por categorias. Abaixo estão documentadas as principais telas e funcionalidades disponíveis.

### 🎬 Tela de Boas-Vindas

**Quando é exibida:** Ao iniciar o sistema pela primeira vez em cada sessão.

**Conteúdo:**
- **Cabeçalho:** CATÁLOGO DE FILMES E SÉRIES
- **Informações do usuário:** Nome e ID do usuário logado
- **Resumo estatístico:**
  - Total de mídias no catálogo
  - Total de filmes cadastrados
  - Total de séries cadastradas
  - Tempo total assistido (em minutos e horas)
- **Lista de comandos disponíveis:** Comandos organizados por categoria

**Exemplo visual:**
```
================================================================================
                    🎬 CATÁLOGO DE MÍDIAS
================================================================================
👤 Usuário: Usuario Padrao (ID: 1)
📊 Resumo: 15 mídias | 8 filmes | 7 séries | ~45h assistidas
--------------------------------------------------------------------------------
```

### 📚 Tela de Catálogo

**Comando:** `midia listar`

**Conteúdo:**
- Lista formatada de todas as mídias cadastradas
- Informações exibidas:
  - ID da mídia
  - Tipo (FILME ou SERIE)
  - Título
  - Média de avaliações (⭐)
  - Gênero
  - Duração (filmes) ou total de temporadas/episódios (séries)

**Formato de exibição:**
```
================================================================================
                           CATÁLOGO DE MÍDIAS
================================================================================
 ID: 1  | [FILME ] Inception              | ⭐ 9.5 | Ficção Científica | 148 min
 ID: 2  | [SERIE ] Breaking Bad           | ⭐ 9.8 | Drama             | 5 Temps | 62 Eps | 2934 min
```

### 📝 Tela de Cadastro de Mídia

**Comando:** `midia adicionar`

**Fluxo:**
1. Solicitação de dados básicos (título, tipo, gênero, ano, classificação, elenco)
2. Dados específicos conforme o tipo:
   - **Filme:** Duração em minutos
   - **Série:** Apenas dados básicos (temporadas e episódios são adicionados depois)

**Validações:**
- Gênero deve estar na lista de gêneros disponíveis
- Classificação deve ser válida (L, 10, 12, 14, 16, 18)
- Verificação de duplicidade (título + ano)

### ⭐ Tela de Avaliação

**Comando:** `midia avaliar`

**Fluxo:**
1. Exibição do catálogo para seleção
2. Seleção da mídia por ID
3. **Para Filmes:** Avaliação direta (nota 0-10 e comentário opcional)
4. **Para Séries:** Seleção de episódio específico e avaliação do episódio

**Dados coletados:**
- Nota (0 a 10)
- Comentário (opcional)
- ID do usuário
- ID da mídia/episódio

### 📊 Tela de Relatórios

**Comando:** `midia relatorio top`

**Conteúdo:**
- **Tempo total assistido:** Separado por tipo (filmes/séries)
- **Média de notas por gênero:** Estatísticas de avaliação
- **Séries mais assistidas:** Ranking por número de episódios assistidos
- **Top 10 mídias:** Ranking das melhores avaliações do catálogo

**Formato:**
```
📊 RELATÓRIOS DE CONSUMO E DESEMPENHO
[ TEMPO TOTAL ASSISTIDO ]
- FILME: 1240 min (~20h)
- SERIE: 2934 min (~48h)

[ MÉDIA DE NOTAS POR GÊNERO ]
- Drama          : ⭐ 9.2
- Ficção Científica: ⭐ 8.9

[ TOP 10 MÍDIAS DO CATÁLOGO ]
1º Breaking Bad        | ⭐ 9.8
2º Inception           | ⭐ 9.5
```

### 📺 Tela de Gerenciamento de Séries

**Comandos:** `serie adicionar-episodio`, `serie atualizar-status`

**Funcionalidades:**
- **Adicionar episódio:** 
  - Seleção da série
  - Número da temporada (criação automática se não existir)
  - Dados do episódio (número, título, duração)
- **Atualizar status:**
  - Lista de episódios disponíveis
  - Seleção de episódio por ID
  - Atualização de status (NÃO ASSISTIDO, ASSISTINDO, ASSISTIDO)

### 🎬 Tela de Gerenciamento de Filmes

**Comando:** `filme atualizar-status`

**Funcionalidades:**
- Lista de filmes cadastrados
- Seleção do filme por ID
- Atualização de status de visualização (NÃO ASSISTIDO, ASSISTINDO, ASSISTIDO)

### 👤 Tela de Gerenciamento de Usuário

**Comandos:** `usuario criar-lista`, `usuario adicionar-favorito`

**Funcionalidades:**
- **Criar lista personalizada:** Criação de listas customizadas (ex: "Assistir depois", "Favoritos")
- **Adicionar favorito:** Marcação de mídias como favoritas

### 💡 Tela de Ajuda

**Comando:** `help` ou `ajuda`

**Conteúdo:**
- Lista completa de todos os comandos disponíveis
- Organização por categorias:
  - 📚 MÍDIA
  - 📺 SÉRIE
  - 🎬 FILME
  - 👤 USUÁRIO
  - ⚙️ SISTEMA
- Descrição breve de cada comando

### 🔄 Fluxo de Navegação

1. **Inicialização:** Tela de boas-vindas com comandos
2. **Operações:** Comandos específicos executam suas respectivas telas
3. **Retorno:** Após cada operação, retorna ao prompt de comandos
4. **Ajuda:** Comando `help` sempre disponível para consulta
5. **Saída:** Comando `sair` encerra o sistema

## 🔗 Referência Principal do Projeto (Link para o Arquivo Base)
**Arquivo Base:** https://docs.google.com/document/d/1Grv7dnrhYA3PhTxRSJIqgxM-UFbGesNb/edit

## Conhecimento adquirido para debate e melhorias

Dentro de cada pasta `src`, `db`, `enum`, deve existir um arquivo vazio chamado __init__.py que avisa ao python que são pacotes e permite que as classes sejam importadas entre si.

### Mensagem de commit
As mensagens de commit podem ser organizadas seguindo uma estrutura básica:

 `escopo: descrição`

`[corpo opcional]`


#### Tipos Principais
- **feat**: Nova funcionalidade
- **fix:** Correção de bug

- **docs:** Mudanças na documentação
- **style:** Formatação, espaços, ponto e vírgula -(sem mudança de código)
- **refactor:** Refatoração de código (sem -0adicionar funcionalidade ou corrigir bug)
- **test:** Adição ou correção de testes
- **chore:** Tarefas de build, configurações, -dependências
- **perf:** Melhorias de performance
- **ci:** Mudanças em CI/CD
- **build:** Mudanças no sistema de build
- **revert:** Reverter um commit anterior

## Ferramentas e Setup

Para baixar o CLI na sua máquina e poder utilizar você pode precisar usar algumas ferramentas:

### tree
comando utilitário de terminal que exibe o conteúdo de um diretório em um formato de árvore gráfica. Ele é extremamente útil para visualizar a hierarquia de pastas e arquivos de um projeto de programação.
Não é obrigatório, mas ajuda na visualização das pastas via terminal

```bash
# No Ubuntu/WSL
sudo apt install tree

# No Mac
brew install tree
```
Usar

```bash
# Árvore completa
tree

# Limitar níveis de profundidade
tree -L 2        # Apenas 2 níveis

# Apenas diretórios (sem arquivos)
tree -d

# Ignorar node_modules, .git, etc
tree -I 'node_modules|.git|__pycache__'
```

### SQLite
Veifiquie se tem o SQLite3 instalado

```bash
sqlite3 --version
```

#### 1. Instalação

```bash
sudo apt update
sudo apt install sqlite3
```

#### 2. Modo interativo
```bash
sqlite3 catalogo.db
```

####  3. Comandos úteis
```sql
-- Ver as tabelas
.tables

-- Ver estrutura da tabela midia
.schema midia

-- Consultar dados
SELECT * FROM midia;

-- Contar registros
SELECT COUNT(*) FROM midia;

-- Sair
.quit
```

### 📂 Estrutura do Projeto
```text
```

### 🚀 Como Rodar
1. **Clone o repositório:**
```bash
git clone https://github.com/saraferreira10/poo-projeto-ufca.git
```

2. **Entre na pasta:**
```bash
cd POO-PROJETO-UFCA
```

3. **Execute o projeto:**
```bash
python3 main.py
```
