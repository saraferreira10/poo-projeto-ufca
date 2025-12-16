# 🎬 Como Rodar o Projeto – Catálogo de Filmes e Séries (FastAPI + SQLModel + SQLite)

## 1️⃣ Clonar o Projeto
```
git clone https://github.com/saraferreira10/poo-projeto-ufca.git
cd poo-projeto-ufca
```


## 2️⃣ Criar Ambiente Virtual

Recomendado para gerenciar dependências:

```
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```


## 3️⃣ Instalar Dependências

Se houver `requirements.txt`:

```bash
pip install -r requirements.txt
```

Exemplo mínimo de `requirements.txt`:

```
fastapi==0.124.4
uvicorn==0.38.0
sqlmodel==0.0.27
```

Se não houver, instale manualmente:

```bash
pip install fastapi uvicorn sqlmodel
```

---

## 4️⃣ Criar o Banco de Dados

No SQLite + SQLModel, crie o banco e as tabelas.

Exemplo `database.py`:

```python
from sqlmodel import SQLModel, create_engine
from app.models.filme import Filme
# outros modelos

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

def criar_tabelas():
    SQLModel.metadata.create_all(engine)
```

Você pode criar as tabelas diretamente:

```bash
python -m app.db.database
```

Ou usando a **lifespan** do FastAPI que cria na inicialização.

---

## 5️⃣ Rodar a API

Use **Uvicorn** para iniciar a API:

```bash
uvicorn app.main:app --reload
```

* `app.main:app` → arquivo `app/main.py`, objeto `app`
* `--reload` → reinicia automaticamente quando houver alterações no código

A API estará disponível em:

```
http://127.0.0.1:8000
```

---

## 6️⃣ Testar a API

O FastAPI cria documentação interativa:

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

Exemplo de endpoints:

* `GET /filmes/` → lista todos os filmes
* `POST /filmes/` → cria um novo filme

---

## 7️⃣ Estrutura do Projeto

```
app/
├── main.py            # Inicializa FastAPI
├── db/
│   ├── database.py    # Engine e criar_tabelas()
├── models/
│   ├── filme.py
│   ├── serie.py
│   ├── episodio.py
├── routes/
│   ├── filmes.py
│   ├── series.py
```

## 8️⃣ Resumo Passo a Passo

1. Clonar e acessar o diretório do projeto
2. Criar e ativar ambiente virtual
3. Instalar dependências (`requirements.txt`)
4. Criar banco de dados/tabelas
5. Rodar API com `uvicorn`
6. Testar endpoints pelo Swagger UI ou ReDoc