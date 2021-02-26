from core.filter import Filter
from core.parser import Parser


class Reader:
    def __init__(self, filters=None, fname='NFe.txt', delimiter=';'):
        self.filters = filters
        self.fname = fname
        self.delimiter = delimiter
        self.filter = Filter()
        self.parser = Parser()
        self.documents = self.read()

    def read(self):
        with open(self.fname, 'r') as f:
            docs = []
            for row in f:
                doc = self.get_doc(row.strip())

                if doc and self.filter(doc, self.filters):
                    docs.append(doc)

            return docs

    def get_doc(self, data):
        values = data.split(self.delimiter)
        return self.parser.parse(values)


def test_must_return_document_by_key():
    d = Reader(filters={'Chave': '72494092851953317464101717301780592482317859'})
    expect = {
        'Data': '13/04/2017',
        'Tipo': 'S',
        'CnpjCpf': '16302620996',
        'Numero': '840634959',
        'Serie': '3',
        'Modelo': '55',
        'Chave': '72494092851953317464101717301780592482317859',
        'ValorTotal': 1992.30,
        'ValorProd': 1932.53,
        'ValorICMS': 347.86,
        'ValorIPI': 154.60,
        'Status': 'AUTORIZADO',
    }
    assert d.documents[0] == expect


if __name__ == '__main__':
    Reader()
