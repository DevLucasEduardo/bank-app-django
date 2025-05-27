from rest_framework.views import APIView
from .models import Client, Account
from .serializers import ClientSerializer, AccountSerializer
from rest_framework.response import Response
from rest_framework import status


class ClientList(APIView):
    def get(self, request, format=None):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)


