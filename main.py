from core.filter import Filter
from core.parsers import DocExtractor


class Reader:
    FILE = 'NFe.txt'
    DELIMITER = ';'

    def __init__(self, filters=None):
        self.filters = filters
        self.filter = Filter()
        self.doc_extract = DocExtractor()
        self.documents = self.get_documents()

    def get_documents(self):
        docs = self.parse_docs()
        docs = self.parse_transactions(docs)
        return docs

    def parse_docs(self):
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
        return self.doc_extract(values)

    def parse_transactions(self, docs):
        return docs


if __name__ == '__main__':
    Reader()
