import pytest

from core.parsers import DocExtractor, TransactionsParser, DocumentsParser


class TestExtractor:
    @pytest.fixture
    def extractor(self):
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
        return DocExtractor().extract(content)

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
    def test_extract(self, extractor, key, expected):
        assert extractor[key] == expected


class TestDocumentsParser:
    def test_parser(self):
        expect = {
            '89958861455662550443256825625984378899008104': {
                'Data': '16/04/2017',
                'Tipo': 'E',
                'CnpjCpf': '04867532983',
                'Numero': '515521624',
                'Serie': '3',
                'Modelo': '55',
                'Chave': '89958861455662550443256825625984378899008104',
                'ValorTotal': 9919.80,
                'ValorProd': 9622.21,
                'ValorICMS': 1732.00,
                'ValorIPI': 769.78,
                'Status': 'AUTORIZADO',
            }
        }
        filters = {'Chave': '89958861455662550443256825625984378899008104'}
        dp = DocumentsParser(filters)
        assert dp.parse() == expect


class TestTransactionsParser:
    def test_parse(self):
        tp = TransactionsParser()
        docs = {'72494092851953317464101717301780592482317859': {}}
        expect = {
            '72494092851953317464101717301780592482317859': {
                'Transacoes': [
                    [
                        '#IdProc 96990 InitTran Início de transação',
                        '#IdProc 220 Log ClientConnect',
                        '#IdProc 41401 Log Chave transação NF-e envolvida: 72494092851953317464101717301780592482317859',
                        '#IdProc 1552 Send NF-e recebida pelo servidor. Gerada requisição para a SEFAZ-SP em modo normal.',
                        '#IdProc 89294 Return A SEFAZ autorizou (Protocolo de autorização 556849) a NF-e com sucesso!',
                        '#IdProc 5513 EndTran Fim de transação',
                    ]
                ]
            }
        }
        assert tp.parse(docs) == expect

    def test_must_extract(self):
        tp = TransactionsParser()
        row = '#IdProc 41401 Log Chave transação NF-e envolvida: 72494092851953317464101717301780592482317859'
        keys = [
            '72494092851953317464101717301780592482317859',
            '89958861455662550443256825625984378899008104',
            '19529899511922440710220225593997181644125803',
        ]
        assert tp.must_extract(row, keys) is True

    def test_get_key(self):
        tp = TransactionsParser()
        row = '#IdProc 41401 Log Chave transação NF-e envolvida: 72494092851953317464101717301780592482317859'
        assert tp.get_key(row) == '72494092851953317464101717301780592482317859'

    def test_add_transaction(self):
        tp = TransactionsParser()
        rows = [
            '#IdProc 96990 InitTran Início de transação',
            '#IdProc 220 Log ClientConnect',
            '#IdProc 41401 Log Chave transação NF-e envolvida: 72494092851953317464101717301780592482317859',
            '#IdProc 1552 Send NF-e recebida pelo servidor. Gerada requisição para a SEFAZ-SP em modo normal.',
            '#IdProc 89294 Return A SEFAZ autorizou (Protocolo de autorização 556849) a NF-e com sucesso!',
            '#IdProc 5513 EndTran Fim de transação',
        ]
        expect = {
            'Transacoes': [
                [
                    '#IdProc 96990 InitTran Início de transação',
                    '#IdProc 220 Log ClientConnect',
                    '#IdProc 41401 Log Chave transação NF-e envolvida: 72494092851953317464101717301780592482317859',
                    '#IdProc 1552 Send NF-e recebida pelo servidor. Gerada requisição para a SEFAZ-SP em modo normal.',
                    '#IdProc 89294 Return A SEFAZ autorizou (Protocolo de autorização 556849) a NF-e com sucesso!',
                    '#IdProc 5513 EndTran Fim de transação',
                ]
            ]
        }
        assert tp.add_transactions(rows, {}) == expect
