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