from pathlib import Path, PurePath

from core.filter import Filter


class DocExtractor:
    DATE_POSITION = 0
    TYPE_POSITION = 1
    PERSONAL_ID_POSITION = 2
    DOCUMENT_NO_POSITION = 3
    SERIE_NO_POSITION = 4
    MODEL_POSITION = 5
    KEY_POSITION = 6
    TOTAL_AMOUNT_POSITION = 7
    PROD_AMOUNT_POSITION = 8
    ICMS_AMOUNT_POSITION = 9
    IPI_AMOUNT_POSITION = 10
    STATUS_POSITION = 11

    def extract(self, content: list):
        try:
            return {
                'Data': content[self.DATE_POSITION],
                'Tipo': content[self.TYPE_POSITION],
                'CnpjCpf': content[self.PERSONAL_ID_POSITION],
                'Numero': content[self.DOCUMENT_NO_POSITION],
                'Serie': content[self.SERIE_NO_POSITION],
                'Modelo': content[self.MODEL_POSITION],
                'Chave': content[self.KEY_POSITION],
                'ValorTotal': self._convert_num(content[self.TOTAL_AMOUNT_POSITION]),
                'ValorProd': self._convert_num(content[self.PROD_AMOUNT_POSITION]),
                'ValorICMS': self._convert_num(content[self.ICMS_AMOUNT_POSITION]),
                'ValorIPI': self._convert_num(content[self.IPI_AMOUNT_POSITION]),
                'Status': content[self.STATUS_POSITION],
            }
        except ValueError:
            pass
        except Exception as e:
            raise e

    @staticmethod
    def _convert_num(n):
        return float(n.replace(',', '.'))


class Parser:
    BASE_DIR = Path(__file__).resolve().parent.parent


class DocumentsParser(Parser):
    FILE = 'NFe.txt'
    DELIMITER = ';'

    def __init__(self, filters=None):
        self.filters = filters
        self.filter = Filter()
        self.extractor = DocExtractor()

    def parse(self):
        docs = {}
        with open(self.FILE, 'r') as f:
            for row in f:
                doc = self.parse_doc(row.strip())

                if doc and self.filter(doc, self.filters):
                    key = doc['Chave']
                    docs[key] = doc

            return docs

    def parse_doc(self, data):
        values = data.split(self.DELIMITER)
        return self.extractor.extract(values)


class TransactionsParser(Parser):
    CONTENT_RANGE = 2

    def __init__(self, file='NFeTran.txt'):
        self.file = file

    def parse(self, docs):
        fpath = PurePath.joinpath(self.BASE_DIR, self.file)
        with open(fpath, 'r') as f:
            must_extract = False
            counter = 0
            key = None

            for row in f:
                if self.key_in_row(row, docs.keys()) or must_extract:
                    if not key:
                        key = self.get_key(row.strip())

                    self.add_transaction(row.strip(), docs[key])

                    must_extract = True
                    counter += 1

                if counter == 3:
                    must_extract = False
                    counter = 0
                    key = None

            return docs

    @staticmethod
    def key_in_row(row, keys):
        return any(key in row for key in keys)

    @staticmethod
    def add_transaction(row, doc):
        if 'Transacoes' not in doc:
            doc['Transacoes'] = []

        doc['Transacoes'].append(row)
        return doc

    @staticmethod
    def get_key(row):
        prefix = 'envolvida: '
        return row.split(prefix)[1]
