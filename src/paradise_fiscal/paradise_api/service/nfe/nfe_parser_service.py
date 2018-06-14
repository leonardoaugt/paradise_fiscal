from .nfe_reader_service import read_file


def parse_file():

    root = {}
    data = read_file('NFe.txt')
    root = nfes_all(root, data)
    return root


def nfes_all(root, data):

    # Get all NFes
    i = 0
    for row in data:
        row_splitted = row.strip().split(';')
        root = get_nfe(root, row_splitted, i)
        i += 1
    f = open('nfes_all.txt', 'w')
    f.write(str(root))
    f.close()


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
        }
    return root


parse_file()