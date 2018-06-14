from rest_framework.views import APIView

from .service.nfe.nfe_service import get_all


class Nfes(APIView):
    def get(self, request):

        response = get_all()
        return response