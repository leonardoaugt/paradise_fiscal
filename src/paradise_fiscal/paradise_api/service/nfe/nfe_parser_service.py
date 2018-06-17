from ..utils.utils import read_file


def nfe_parse_file(filter=None, column=None):

    root = {}
    data = read_file('NFe.txt')
    data.pop(0) # Remove headers
    if filter and column:
        root = apply_filter(root, data, filter, column)
    else:
        root = nfes_all(root, data)
    return root



def apply_filter(root, data, filter, column):

    # Filter NFes
    i = 1
    for row in data:
        row_splitted = row.strip().split(';')
        if filter_validate(filter, column, row_splitted):
            root = get_nfe(root, row_splitted, i)
        i += 1
    return root



def filter_validate(filter, column, row_splitted):

    # Validate filter
    if filter == row_splitted[column]:
        return True
    return False



def nfes_all(root, data):

    # Get all NFes
    i = 1
    for row in data:
        row_splitted = row.strip().split(';')
        root = get_nfe(root, row_splitted, i)
        i += 1
    return root



def get_nfe(root, row_splitted, i):

    # Make NFe object
    root['NFe_{}'.format(i)] = {
        'Data': row_splitted[0],
        'Tipo': row_splitted[1],
        'CnpjCpf': row_splitted[2],
        'Numero': row_splitted[3],
        'Serie': row_splitted[4],
        'Modelo': row_splitted[5],
        'Chave': row_splitted[6],
        'ValorTotal': row_splitted[7],
        'ValorProd': row_splitted[8],
        'ValorICMS': row_splitted[9],
        'ValorIPI': row_splitted[10],
        'Status': row_splitted[11],
        'Totalizador': get_amount(row_splitted, 7, 8, 9, 10)
        }
    return root



def get_amount(row_splitted, *args):

    # amount = ValorTotal + ValorProd + ValorICMS + ValorIPI
    amount = 0
    for arg in args:
        value = float(row_splitted[arg].replace(',', '.'))
        amount += value
    amount = str(round(amount, 2)).replace('.', ',')
    return amount

