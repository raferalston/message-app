from rest_framework import viewsets
from rest_framework.response import Response

from .models import ClientModel
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
