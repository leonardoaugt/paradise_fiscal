
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.authentication import get_authorization_header

from .nfetran_parser_service import nfetran_parse_file, get_by_key
from ..nfe.nfe_parser_service import nfe_parse_file


def get_nfetran():

    data = nfetran_parse_file()
    if data:
        return Response({'Dados': data}, HTTP_200_OK)
    return Response({'Erro': 'Nenhum documento encontrado'}, HTTP_404_NOT_FOUND)


def get_nfetran_key(key):

    key = str(key)
    nfetran = get_by_key(key)
    if nfetran:
        nfe_key = nfetran_parse_file(key, 6)
        if nfe_key:
            merged = {**nfe_key, **nfetran}
            return Response({'Dados': merged}, HTTP_200_OK)
    return Response({'Erro': 'Documento não encontrado'}, HTTP_404_NOT_FOUND)