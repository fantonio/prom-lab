from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ClientesList(APIView):

    count = 0

    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        ClientesList.count = ClientesList.count + 1
        serializer = ClienteSerializer(data=request.data)
        if(ClientesList.count == 11):
            ClientesList.count = 0
            return Response("Serviço indisponível", status=status.HTTP_503_SERVICE_UNAVAILABLE)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)