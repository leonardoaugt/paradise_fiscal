
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.authentication import get_authorization_header

from .nfe_parser_service import parse_file


def get_all():

    data = parse_file()
    if data:
        return Response({'Dados': data}, HTTP_200_OK)
    return Response({'Dados': 'Nenhum documento encontrado.'}, HTTP_404_NOT_FOUND)


def get_filter(filter, column):
    
    data = parse_file(filter, column)
    if data:
        return Response({'Dados': data}, HTTP_200_OK)
    return Response({'Dados': 'Documento não encontrado'}, HTTP_404_NOT_FOUND)
