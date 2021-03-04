from datetime import datetime


class Filter:
    def __call__(self, doc, filters):
        if doc and filters['Chave']:
            if doc['Chave'] == filters['Chave']:
                return doc

        if doc and filters['DataInicio'] and filters['DataFim']:

            def to_python(date):
                return datetime.date(datetime.strptime(date, '%d/%m/%Y'))

            start = to_python(filters['DataInicio'])
            end = to_python(filters['DataFim'])
            ref = to_python(doc['Data'])

            if start <= ref <= end:
                return doc
