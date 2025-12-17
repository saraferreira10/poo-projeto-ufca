# 🎬 Como Rodar o Projeto – Catálogo de Filmes e Séries

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


```bash
pip install -r requirements.txt
```

## 4️⃣ Rodar a API

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

## 5️⃣ Testar a API

O FastAPI cria documentação interativa:

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

Exemplo de endpoints:

* `GET /filmes/` → lista todos os filmes
* `POST /filmes/` → cria um novo filme

---

## 6️⃣ Estrutura do Projeto

```
poo-projeto-ufca/
├── app/
│   ├── main.py
│   ├── db/  # Contém tudo relacionado à persistência de dados (SQLite)
│   │   └── dados.py
│   ├── models/  # Contém as classes do domínio (POO)
│   │   ├── midia.py
│   │   ├── filme.py
│   │   ├── serie.py
│   │   ├── temporada.py
│   │   └── episodio.py
│   ├── crud/ # Contém funções de CRUD para cada model, responsáveis por interagir com o banco
│   │   └── midia_crud.py
│   ├── dto/ # Contém schemas Pydantic para validação de dados enviados/recebidos pela API
│   │   └── midia_dto.py
│   └── routes/ # Contém os endpoints da API
│       └── midia_routes.py
```

## 7️⃣ Resumo Passo a Passo

1. Clonar e acessar o diretório do projeto
2. Criar e ativar ambiente virtual
3. Instalar dependências (`requirements.txt`)
4. Rodar API com `uvicorn`
5. Testar endpoints pelo Swagger UI ou ReDoc
