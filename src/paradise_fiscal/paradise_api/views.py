from django.shortcuts import render

from .service.nfe.nfe_service import get_all

class Nfes(APIView):
    def get(self, request):

        return get_all()