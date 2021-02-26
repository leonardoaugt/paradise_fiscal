import pytest


class Parser:
    DATE_POSITION = 0
    TYPE_POSITION = 1
    PERSONAL_ID_POSITION = 2
    DOCUMENT_NO_POSITION = 3
    SERIE_NO_POSITION = 4
    MODEL_POSITION = 5
    KEY_POSITION = 6
    TOTAL_AMOUNT_POSITION = 7
    PROD_AMOUNT_POSITION = 8
    ICMS_AMOUNT_POSITION = 9
    IPI_AMOUNT_POSITION = 10
    STATUS_POSITION = 11

    def parse(self, content: list):
        return self.make_dict(content)

    def make_dict(self, content):
        try:
            return {
                'Data': content[self.DATE_POSITION],
                'Tipo': content[self.TYPE_POSITION],
                'CnpjCpf': content[self.PERSONAL_ID_POSITION],
                'Numero': content[self.DOCUMENT_NO_POSITION],
                'Serie': content[self.SERIE_NO_POSITION],
                'Modelo': content[self.MODEL_POSITION],
                'Chave': content[self.KEY_POSITION],
                'ValorTotal': self._convert_num(content[self.TOTAL_AMOUNT_POSITION]),
                'ValorProd': self._convert_num(content[self.PROD_AMOUNT_POSITION]),
                'ValorICMS': self._convert_num(content[self.ICMS_AMOUNT_POSITION]),
                'ValorIPI': self._convert_num(content[self.IPI_AMOUNT_POSITION]),
                'Status': content[self.STATUS_POSITION],
            }
        except ValueError:
            pass
        except Exception as e:
            raise e

    @staticmethod
    def _convert_num(n):
        return float(n.replace(',', '.'))


@pytest.fixture
def parser():
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
    return Parser().parse(content)


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
def test_parser(parser, key, expected):
    assert parser[key] == expected
