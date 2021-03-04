from datetime import datetime


class Filter:
    def __call__(self, doc, filters):
        if doc and filters['Chave']:
            if doc['Chave'] == filters['Chave']:
                return doc

        if doc and filters['DataInicio'] and filters['DataFim']:
            start = datetime.date(datetime.strptime(filters['DataInicio'], '%d/%m/%Y'))
            end = datetime.date(datetime.strptime(filters['DataFim'], '%d/%m/%Y'))
            ref = datetime.date(datetime.strptime(doc['Data'], '%d/%m/%Y'))
            if start <= ref <= end:
                return doc
