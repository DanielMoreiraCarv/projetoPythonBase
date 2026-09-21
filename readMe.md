from pathlib import Path

conteudo = r"""# GUIA RÁPIDO — BAIXAR E RODAR O PROJETO FASTAPI

## 1. CLONAR O PROJETO

git clone URL_DO_REPOSITORIO

cd NOME_DO_PROJETO


## 2. CRIAR O AMBIENTE VIRTUAL

python -m venv .venv


## 3. ATIVAR O AMBIENTE VIRTUAL

### Windows CMD

.venv\Scripts\activate

### bash

source .venv/Scripts/activate

### Windows PowerShell

.\.venv\Scripts\Activate.ps1


## 4. ATUALIZAR O PIP

python -m pip install --upgrade pip


## 5. INSTALAR AS DEPENDÊNCIAS

Se existir o arquivo requirements.txt:

pip install -r requirements.txt

Caso NÃO exista:

pip install fastapi uvicorn sqlalchemy "psycopg[binary]" pydantic


## 6. CONFIGURAR O POSTGRESQL

A aplicação utiliza PostgreSQL local.

Configuração utilizada:

Host: localhost
Porta: 5432
Banco: postgres
Usuário: postgres

Configure a senha no arquivo de conexão.

Exemplo:

DATABASE_URL = "postgresql+psycopg://postgres:SENHA@localhost:5432/postgres"


## 7. CRIAR AS TABELAS

Execute o script SQL do projeto no PostgreSQL.

Tabelas principais:

py_produto
py_estoque
py_aux_produto_estoque
py_registro_movimentacao
py_auditoria


## 8. INICIAR A API

Na raiz do projeto e com o .venv ativado:

uvicorn app.main:app --reload

### ou :
uv run uvicorn app.main:app --reload

### via docker:
docker start gestao-patrimonio-api

### acompanhar logs por docker:
docker logs -f gestao-patrimonio-api


![alt text](image.png)



## 9. ACESSAR O SWAGGER

http://localhost:8000/docs


## 10. ACESSAR O REDOC

http://localhost:8000/redoc


## 11. PARAR A API

CTRL + C


## 12. SAIR DO AMBIENTE VIRTUAL

deactivate


# COMANDOS DO DIA A DIA

cd NOME_DO_PROJETO

.venv\Scripts\activate

uvicorn app.main:app --reload


# PRIMEIRA INSTALAÇÃO — RESUMO

git clone URL_DO_REPOSITORIO
cd NOME_DO_PROJETO
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload


# SE NÃO EXISTIR requirements.txt

git clone URL_DO_REPOSITORIO
cd NOME_DO_PROJETO
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy "psycopg[binary]" pydantic
uvicorn app.main:app --reload


# IMPORTANTE

O comando:

uvicorn app.main:app --reload

significa:

app.main = arquivo app/main.py
app = objeto FastAPI criado dentro do main.py
--reload = reinicia automaticamente a API quando o código for alterado


# ESTRUTURA MÍNIMA ESPERADA

projeto/
│
├── app/
│   ├── main.py
│   ├── controller/
│   ├── service/
│   ├── repository/
│   ├── model/
│   └── database/
│
├── .venv/
└── requirements.txt


# GIT — ATUALIZAR O PROJETO

git pull

Se houver alterações locais e você quiser descartá-las antes:

git restore .

git pull


# GIT — INSTALAR DEPENDÊNCIAS NOVAS

Sempre que o requirements.txt for atualizado:

pip install -r requirements.txt


# GERAR/ATUALIZAR requirements.txt

pip freeze > requirements.txt
"""

caminho = Path("/mnt/data/guia_comandos_fastapi.txt")
caminho.write_text(conteudo, encoding="utf-8")

print(caminho)


## Script base para as tabelas

```sql
CREATE TABLE public.py_produto (
    id BIGSERIAL PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    marca VARCHAR(255),
    dt_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dt_alteracao TIMESTAMP,
    dt_delecao TIMESTAMP
);

CREATE TABLE public.py_estoque (
    id BIGSERIAL PRIMARY KEY,
    cep VARCHAR(8) NOT NULL,
    numero_local INT NOT NULL,
    telefone VARCHAR(20),
    dt_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dt_alteracao TIMESTAMP,
    dt_delecao TIMESTAMP
);

CREATE TABLE public.py_aux_produto_estoque (
    id BIGSERIAL PRIMARY KEY,
    id_produto BIGINT NOT NULL,
    id_estoque BIGINT NOT NULL,
    quantidade INT NOT NULL DEFAULT 0,

    CONSTRAINT fk_aux_prod
        FOREIGN KEY (id_produto)
        REFERENCES public.py_produto(id),

    CONSTRAINT fk_aux_est
        FOREIGN KEY (id_estoque)
        REFERENCES public.py_estoque(id),

    CONSTRAINT uk_produto_estoque
        UNIQUE (id_produto, id_estoque),

    CONSTRAINT ck_quantidade_positiva
        CHECK (quantidade >= 0)
);

CREATE TABLE public.py_registro_movimentacao (
    id BIGSERIAL PRIMARY KEY,
    id_produto BIGINT NOT NULL,
    id_estoque_chegada BIGINT,
    id_estoque_saida BIGINT,
    quantidade INT NOT NULL,
    dt_movimentacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dsc_responsavel VARCHAR(255) NOT NULL,
    tip_movimentacao INT NOT NULL,

    CONSTRAINT fk_mov_prod
        FOREIGN KEY (id_produto)
        REFERENCES public.py_produto(id),

    CONSTRAINT fk_mov_est_chegada
        FOREIGN KEY (id_estoque_chegada)
        REFERENCES public.py_estoque(id),

    CONSTRAINT fk_mov_est_saida
        FOREIGN KEY (id_estoque_saida)
        REFERENCES public.py_estoque(id),

    CONSTRAINT ck_mov_quantidade
        CHECK (quantidade > 0),

    CONSTRAINT ck_tipo_movimentacao
        CHECK (tip_movimentacao IN (0, 1, 2))
);

CREATE TABLE public.py_auditoria (
    id BIGSERIAL PRIMARY KEY,
    tabela VARCHAR(100) NOT NULL,
    registro_id BIGINT NOT NULL,
    operacao VARCHAR(20) NOT NULL,
    usuario VARCHAR(255),
    descricao TEXT,
    dt_operacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM public.py_auditoria;

ALTER USER postgres WITH PASSWORD '12345';
```
# CONEXÃO UTILIZADA PELO PYTHON

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/postgres"



