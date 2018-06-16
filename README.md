#Paradise Fiscal

## Requisitos ##
Python 3.5 ou superior https://www.python.org/downloads/
virtualenv https://virtualenv.pypa.io/en/stable/installation/

## Configurando o ambiente ##
Após clonar o repositório, no diretório /src rode o comando `virtualenv .` para instalar o ambiente python isolado.

## Instalação ##
Para instalar as dependências do projeto, rode o comando `pip install -r requirements.txt`

## API ##
Para rodar a aplicação, certifique-se de estar no mesmo diretório do arquivo manager.py, e rode o comando `python manage.py runserver`.
A aplicação irá rodar em `http://localhost:8000`
##Métodos disponíveis
###Transações
api/nfetran/transacoes/
api/nfetran/transacao/chave/[parametro]
###Documentos
api/nfe/all/
api/nfe/tipo/[parametro]
api/nfe/chave/[parametro]
api/nfe/cnpjcpf/[parametro]
api/nfe/status/[parametro]