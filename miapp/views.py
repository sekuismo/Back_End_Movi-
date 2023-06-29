from rest_framework import generics
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import Usuarios


#consulta todos los datos y se le puede agregar un query string para cada id de usuario
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset= Usuarios.objects.all()


# #vista para crear usuarios
# class UsuarioCreateView(generics.CreateAPIView):
#     serializer_class = UserSerializer

# #vista para listar usuarios
# class UsuarioListView(generics.ListAPIView):
#     serializer_class = UserSerializer
#     queryset = Usuarios.objects.all()