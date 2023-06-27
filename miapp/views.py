from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Usuarios


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset= Usuarios.objects.all()