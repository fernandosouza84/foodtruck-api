# foodtruck-api

API para gerenciamento de food trucks, construída com [FastAPI](https://fastapi.tiangolo.com/).

## Stack

| Componente | Versão |
|---|---|
| Python | 3.14 (fixado em `.python-version`) |
| FastAPI | 0.162.5 |
| Uvicorn (servidor ASGI) | 0.54.0 |
| pytest | 9.2.0 |

## Pré-requisitos

- **Git**
- **[uv](https://docs.astral.sh/uv/)** — gerencia a versão do Python e as dependências. Não exige sudo nem altera o Python do sistema.

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

  Depois abra um novo terminal e confira com `uv --version`.

> Já tem Python 3.14 instalado e prefere não usar o uv? Veja [Setup sem uv](#setup-sem-uv).

## Começando

```bash
# 1. Clonar o repositório
git clone git@github.com:fernandosouza84/foodtruck-api.git
cd foodtruck-api

# 2. Instalar o Python 3.14 (se ainda não tiver)
uv python install 3.14

# 3. Criar o ambiente virtual
uv venv --python 3.14 venv

# 4. Ativar o ambiente virtual
source venv/bin/activate          # Linux/macOS
# venv\Scripts\activate           # Windows

# 5. Instalar as dependências (produção + desenvolvimento)
uv pip install -r requirements-dev.txt
```

## Executando a API

Com o ambiente virtual ativado:

```bash
uvicorn main:app --reload
```

O `--reload` reinicia o servidor automaticamente quando o código muda. Use só em desenvolvimento.

| URL | O que é |
|---|---|
| http://localhost:8000 | API |
| http://localhost:8000/docs | Documentação interativa (Swagger UI) |
| http://localhost:8000/redoc | Documentação alternativa (ReDoc) |

Para usar outra porta: `uvicorn main:app --reload --port 8080`.

### Endpoints disponíveis

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Verificação básica: retorna `{"Hello": "World"}` |
| `GET` | `/items/{item_id}?q=` | Exemplo com parâmetro de rota (`int`) e query string opcional |

Teste rápido pela linha de comando:

```bash
curl http://localhost:8000/
curl "http://localhost:8000/items/5?q=taco"
```

## Testes

```bash
pytest          # roda todos os testes
pytest -v       # mostra cada teste
```

Os testes ficam em `tests/` e usam o `TestClient` do FastAPI, que chama a aplicação sem precisar subir o servidor.

## Estrutura do projeto

```
foodtruck-api/
├── main.py                # aplicação FastAPI e rotas
├── tests/
│   └── test_main.py       # testes das rotas
├── requirements.txt       # dependências de produção
├── requirements-dev.txt   # dependências de desenvolvimento (inclui requirements.txt)
├── pytest.ini             # configuração do pytest
└── .python-version        # versão do Python usada no projeto
```

## Dependências

- **`requirements.txt`**: o que a API precisa para rodar. Use em produção.
- **`requirements-dev.txt`**: inclui o `requirements.txt` e acrescenta as ferramentas de teste.

Para adicionar um pacote, coloque-o com versão fixa (`pacote==x.y.z`) no arquivo adequado e reinstale:

```bash
uv pip install -r requirements-dev.txt
```

## Setup sem uv

Se o Python 3.14 já estiver instalado no sistema:

```bash
python3.14 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

Os comandos de execução e de testes são os mesmos.

## Problemas comuns

| Sintoma | Causa provável | Solução |
|---|---|---|
| `uvicorn: command not found` ou `pytest: command not found` | Ambiente virtual não ativado | `source venv/bin/activate` |
| `ModuleNotFoundError: No module named 'fastapi'` | Dependências não instaladas no venv | `uv pip install -r requirements-dev.txt` |
| `[Errno 98] Address already in use` | Porta 8000 ocupada | Use outra porta: `--port 8080` |
| `uv: command not found` logo após instalar | Terminal aberto antes da instalação | Abra um novo terminal |
| No terminal do VS Code (snap), o uv instala o Python dentro de `~/snap/code/...` | O VS Code em snap redireciona `XDG_DATA_HOME` | Rode o uv num terminal comum ou defina `export UV_PYTHON_INSTALL_DIR=~/.local/share/uv/python UV_PYTHON_BIN_DIR=~/.local/bin` |
