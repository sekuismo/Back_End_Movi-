from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer,MovieListSerializer,MovieSerializer
from .models import Usuarios,Peliculas,ListaDePeliculas

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from datetime import timedelta
from django.contrib.auth.hashers import make_password


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuarios.objects.all()

class PeliculasViewSet(viewsets.ModelViewSet):
    queryset = Peliculas.objects.all()
    serializer_class = MovieSerializer

class ListaDePeliculasViewSet(viewsets.ModelViewSet):
    queryset = ListaDePeliculas.objects.all()
    serializer_class = MovieListSerializer
def create(self, request, *args, **kwargs):
    user_id = request.data.get('user')
    movie_id = request.data.get('movie_id')  # Actualizamos el nombre del campo a movie_id
    
    try:
        user = Usuarios.objects.get(id=user_id)
        movie = Peliculas.objects.get(id=movie_id)
    except (Usuarios.DoesNotExist, Peliculas.DoesNotExist):
        return Response({'error': 'User or movie does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    
    lista_data = {
        'user': user.id,
        'movie': movie.id,
        'is_viewed': request.data.get('is_viewed', False),
        'is_erased': request.data.get('is_erased', False),
    }

    lista_serializer = self.get_serializer(data=lista_data)
    lista_serializer.is_valid(raise_exception=True)
    lista_serializer.save()
    
    return Response(lista_serializer.data, status=status.HTTP_201_CREATED)


class CreateUserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuarios.objects.none()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        plain_password = data['password']
        data['password'] = make_password(data['password'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class LoginView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generar tokens de acceso y actualización
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                # Agrega cualquier otra información necesaria para identificar al usuario
            }
            return Response(response_data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


#se invalida el token en vez de utilizar el método logout() de Django

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.set_jti()
            token.set_exp(lifetime=timedelta(seconds=0))

            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
