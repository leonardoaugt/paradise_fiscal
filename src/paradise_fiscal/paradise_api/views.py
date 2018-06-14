from rest_framework.views import APIView

from .service.nfe.nfe_service import get_all, get_filter


class Nfes(APIView):
    def get(self, request):

        response = get_all()
        return response


class NfeType(APIView):
    def get(self, request, type):

        column = 1
        type = type.upper()
        response = get_filter(type, column)
        return response


class NfeKey(APIView):
    def get(self, request, key):

        column = 6
        response = get_filter(key, column)
        return response


class NfePersonalDocument(APIView):
    def get(self, request, personal_doc):
        
        column = 2
        response = get_filter(personal_doc, column)
        return response


class NfeStatus(APIView):
    def get(self, request, status):

        column = 11
        status = status.upper()
        response = get_filter(status, column)
        return response


class NfeTran(APIView):
    def get(self, request):

        response = get_nfetran()
        return response


class NfeTranKey(APIView):
    def get(self, request, key):

        response = get_nfetran_key(key)
        return response
