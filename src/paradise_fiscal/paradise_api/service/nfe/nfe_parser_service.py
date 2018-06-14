
from .nfe_reader_service import read_file


def parse_file():

    data = read_file('NFe.txt')
    data = nfes_all(data)

def nfes_all(data):

    for row in data:
        row_splitted = row.strip().split(';')
        return data
