# Paradise Fiscal

[![Tests](https://github.com/sleonardoaugusto/paradise_fiscal/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/sleonardoaugusto/paradise_fiscal/actions/workflows/ci-cd.yaml)

Parser de arquivos fiscais e transações

## How to setup
1. Clone this repo;
2. Crie um virtualenv com Python 3.7.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:sleonardoaugusto/paradise_fiscal.git
cd paradise_fiscal
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest
```