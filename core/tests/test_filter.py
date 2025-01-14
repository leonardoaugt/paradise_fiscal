import pytest

from core.filter import Filter


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


class TestKeyFilter:
    def test_should_return_document(self, document):
        filters = {
            'Chave': '72494092851953317464101717301780592482317859',
            'DataInicio': '',
            'DataFim': '',
        }
        filter = Filter()
        assert filter(document, filters) == document

    def test_should_return_none(self, document):
        filters = {
            'Chave': '89958861455662550443256825625984378899008104',
            'DataInicio': '',
            'DataFim': '',
        }
        filter = Filter()
        assert filter(document, filters) is None


class TestDateFilter:
    def test_should_return_document(self, document):
        filters = {'Chave': '', 'DataInicio': '13/04/2017', 'DataFim': '16/04/2017'}
        filter = Filter()
        assert filter(document, filters) == document

    def test_should_return_none(self, document):
        filters = {'Chave': '', 'DataInicio': '14/04/2017', 'DataFim': '16/04/2017'}
        filter = Filter()
        assert filter(document, filters) is None
