from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from . import serializers
from rest_framework import permissions


class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class HelloView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
