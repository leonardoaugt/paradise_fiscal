class Filter:
    def __call__(self, doc, filters):
        if doc and filters['Chave']:
            if doc['Chave'] == filters['Chave']:
                return doc
