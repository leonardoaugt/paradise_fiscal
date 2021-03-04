from datetime import datetime


class Filter:
    def __call__(self, doc, filters):
        self.doc = doc
        self.filters = filters
        return self.doc and self.filter_by_key() and self.filter_by_date()

    def filter_by_date(self):
        if not self.filters['DataInicio'] and not self.filters['DataFim']:
            return self.doc

        if self.filters['DataInicio'] and self.filters['DataFim']:

            def to_python(date):
                return datetime.date(datetime.strptime(date, '%d/%m/%Y'))

            start = to_python(self.filters['DataInicio'])
            end = to_python(self.filters['DataFim'])
            ref = to_python(self.doc['Data'])

            if start <= ref <= end:
                return self.doc

    def filter_by_key(self):
        if not self.filters['Chave']:
            return self.doc

        if self.filters['Chave']:
            if self.doc['Chave'] == self.filters['Chave']:
                return self.doc
