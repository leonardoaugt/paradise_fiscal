import re
from pathlib import Path, PurePath

from core.filter import Filter


class InvoiceExtractor:
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


class InvoicesParser(Parser):
    def __init__(self, file, delimiter=';', filters=None):
        self.file = file
        self.delimiter = delimiter
        self.filters = filters
        self.filter = Filter()
        self.extractor = InvoiceExtractor()

    def parse(self):
        docs = {}
        with open(self.file, 'r') as f:
            for row in f:
                doc = self.parse_doc(row.strip())

                if doc and self.filter(doc, self.filters):
                    key = doc['Chave']
                    docs[key] = doc

            return docs

    def parse_doc(self, data):
        values = data.split(self.delimiter)
        return self.extractor.extract(values)


class TransactionsParser(Parser):
    def __init__(self, file):
        self.file = file

    def parse(self, docs):
        fpath = PurePath.joinpath(self.BASE_DIR, self.file)
        with open(fpath, 'r') as f:
            transactions = ''

            for row in f:
                transactions = transactions + row

                if 'EndTran' in row:
                    if self.should_extract(transactions, docs.keys()):
                        key = self.get_key(transactions.strip())
                        self.add_transactions(transactions, docs[key])

                    transactions = ''

            return docs

    @staticmethod
    def should_extract(key, keys):
        return any(k in key for k in keys)

    @staticmethod
    def add_transactions(rows, doc):
        prefix = 'Transacoes'

        if prefix not in doc:
            doc[prefix] = []

        doc[prefix].append(rows)
        return doc

    @staticmethod
    def get_key(content):
        pattern = '(.*)'
        starts_with = 'NF-e envolvida:'
        result = re.search(f"{starts_with}{pattern}", content)
        return result.group(1).strip()
