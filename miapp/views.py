from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Usuarios
from django.contrib.auth import authenticate, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from django.contrib.auth.hashers import make_password


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuarios.objects.all()



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
        print(f"Username: {username}")
        print(f"Password: {password}")

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


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)
