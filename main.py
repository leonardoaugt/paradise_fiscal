from core.parsers import DocumentsParser, TransactionsParser


class Reader:
    def __init__(self, filters=None):
        self.documents_parser = DocumentsParser(filters)
        self.transactions = TransactionsParser()
        self.documents = self.get_documents()

    def get_documents(self):
        docs = self.documents_parser.parse()
        docs = self.transactions.parse(docs)
        return docs


if __name__ == '__main__':
    Reader()
