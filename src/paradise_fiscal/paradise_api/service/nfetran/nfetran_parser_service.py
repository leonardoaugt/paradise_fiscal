
from ..utils.utils import read_file


def get_by_key(key):
    
    data = read_file('NFeTran.txt')
    root = {}
    for row in data:
        if 'Chave' in row:
            key_row = row.split(' ')[7].strip()
            if str(key) == key_row:
                idproc = get_idproc(row)
                break
    transactions = get_transactions(data, idproc)
    root['chave_{}'.format(key)] = transactions
    return root


def get_transactions(data, idproc):

    transactions = []
    for row in data:
        if idproc in row:
            row_idproc = get_idproc(row)
            if row_idproc == idproc:
                transactions.append(row)
    return transactions


def parse_file():
    
    root = {
        'total_transacoes': 0,
        'total_autorizadas': 0,
        'total_canceladas': 0,
        'total_rejeitadas': 0,
        'estatistica_erros': {},
        'estatistica_uf': {},
    }

    data = read_file('NFeTran.txt')
    ufs = get_ufs(data)
    for row in data:
        idproc = str(get_idproc(row))
        if idproc in ufs:
            uf = ufs[idproc]
            if 'InitTran' in row:
                root['total_transacoes'] += 1
                root = check_uf(root, uf)
                root['estatistica_uf'][uf]['transacoes'] += 1

            if 'sucesso' in row:
                root['total_autorizadas'] += 1
                root = check_uf(root, uf)
                root['estatistica_uf'][uf]['autorizadas'] += 1

            if 'cancelamento' in row:
                root['total_canceladas'] += 1
                root = check_uf(root, uf)
                root['estatistica_uf'][uf]['canceladas'] += 1

            if 'rejeitou' in row:
                root['total_rejeitadas'] += 1
                reason = get_reason(row)
                root = check_uf(root, uf)
                root['estatistica_uf'][uf]['rejeitadas'] += 1
                root = check_uf_reason(root, uf, reason)
                root['estatistica_uf'][uf]['motivos']['motivo_{}'.format(reason)] += 1
                root = check_reason(root, reason)
                root['estatistica_erros']['motivo_{}'.format(reason)] += 1
    return root


def get_ufs(data):
    ufs = {}
    for row in data:
        if 'SEFAZ-' in row:
            ufs[get_idproc(row)] = get_uf(row)
    return ufs


def get_idproc(row):
    idproc = str(row.split(' ')[1])
    return idproc


def get_uf(row):
    uf = row.split(' ')[11][-2:]
    return uf


def get_reason(row):
    reason_id = row.split(' ')[11].replace('\n', '')
    return reason_id


def check_uf(root, uf):
    if not uf in root['estatistica_uf']:
        root = insert_uf(root, uf)
    return root


def insert_uf(root, uf):

    root['estatistica_uf'][uf] = {'transacoes': 0,
                                  'autorizadas': 0,
                                  'rejeitadas': 0,
                                  'canceladas': 0,
                                  'motivos': {}}
                                  
    return root


def check_reason(root, reason):
    if not reason in root['estatistica_erros']:
        root = insert_reason(root, reason)
    return root



def insert_reason(root, reason):
    root['estatistica_erros']['motivo_{}'.format(reason)] = 0
    return root



def check_uf_reason(root, uf, reason):
    if not reason in root['estatistica_uf'][uf]['motivos']:
        root = insert_uf_reason(root, uf, reason)
    return root


def insert_uf_reason(root, uf, reason):
    root['estatistica_uf'][uf]['motivos']['motivo_{}'.format(reason)] = 0
    return root