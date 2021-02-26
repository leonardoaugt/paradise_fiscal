import pytest


class Filter:
    def __call__(self, doc, filters):
        if doc and filters['Chave']:
            if doc['Chave'] == filters['Chave']:
                return doc


@pytest.fixture
def document():
    return {
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


def test_must_return_document(document):
    filters = {'Chave': '72494092851953317464101717301780592482317859'}
    filter = Filter()
    assert filter(document, filters) == document


def test_must_return_none(document):
    filters = {'Chave': '89958861455662550443256825625984378899008104'}
    filter = Filter()
    assert filter(document, filters) is None
