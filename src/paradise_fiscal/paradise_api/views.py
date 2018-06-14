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
        filtered_data = get_filter(key, column)
        return filtered_data


class NfePersonalDocument(APIView):
    def get(self, request, personal_doc):
        
        column = 2
        filtered_data = get_filter(personal_doc, column)
        return filtered_data


class NfeStatus(APIView):
    def get(self, request, status):

        column = 11
        status = status.upper()
        filtered_data = get_filter(status, column)
        return filtered_data
