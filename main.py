from core.parsers import InvoicesParser, TransactionsParser


class Reader:
    def __init__(
        self, filters=None, invoices_file='NFe.txt', transactions_file='NFeTran.txt'
    ):
        self.invoices_parser = InvoicesParser(file=invoices_file, filters=filters)
        self.transactions_parser = TransactionsParser(file=transactions_file)
        self.invoices = self.get_invoices()

    def get_invoices(self):
        docs = self.invoices_parser.parse()
        return self.transactions_parser.parse(docs)


if __name__ == '__main__':
    Reader()
