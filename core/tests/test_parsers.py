import pytest

from core.parsers import DocExtractor, TransactionsParser


class TestExtractor:
    @pytest.fixture
    def parser(self):
        content = [
            '16/04/2017',
            'E',
            '04867532983',
            '515521624',
            '3',
            '55',
            '89958861455662550443256825625984378899008104',
            '9919,80',
            '9622,21',
            '1732,00',
            '769,78',
            'AUTORIZADO',
        ]
        return DocExtractor()(content)

    @pytest.mark.parametrize(
        'key,expected',
        [
            ('Data', '16/04/2017'),
            ('Tipo', 'E'),
            ('CnpjCpf', '04867532983'),
            ('Numero', '515521624'),
            ('Serie', '3'),
            ('Modelo', '55'),
            ('Chave', '89958861455662550443256825625984378899008104'),
            ('ValorTotal', 9919.80),
            ('ValorProd', 9622.21),
            ('ValorICMS', 1732.00),
            ('ValorIPI', 769.78),
            ('Status', 'AUTORIZADO'),
        ],
    )
    def test_document_parser(self, parser, key, expected):
        assert parser[key] == expected


class TestTransactionsParser:
    @pytest.mark.skip('')
    def test_parse_transactions(self):
        tp = TransactionsParser()
        docs = {'72494092851953317464101717301780592482317859': {}}
        expect = {
            '72494092851953317464101717301780592482317859': {
                'Transacoes': [
                    '# IdProc 41401 Log Chave transação NF-e envolvida: 72494092851953317464101717301780592482317859'
                    '# IdProc 1552 Send NF-e recebida pelo servidor. Gerada requisição para a SEFAZ-SP em modo normal.'
                    '# IdProc 89294 Return A SEFAZ autorizou (Protocolo de autorização 556849) a NF-e com sucesso!'
                ]
            }
        }
        assert tp(docs) == expect
