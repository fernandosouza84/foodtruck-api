# foodtruck-api
Management foodtrucks

## Requisitos

- Python 3.14 (versão fixada em `.python-version`)
- [uv](https://docs.astral.sh/uv/) (recomendado) ou `venv` + `pip`

## Setup

```bash
uv venv --python 3.14 venv
source venv/bin/activate
uv pip install -r requirements-dev.txt   # ou: pip install -r requirements-dev.txt
```

Use `requirements.txt` sozinho para instalar apenas as dependências de produção.

## Executar

```bash
uvicorn main:app --reload
```

API em http://localhost:8000 — documentação interativa em http://localhost:8000/docs

## Testes

```bash
pytest
```
