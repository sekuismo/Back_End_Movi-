from rest_framework import serializers
from .models import Usuarios, Peliculas, ListaDePeliculas

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peliculas
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = ListaDePeliculas
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    movie_lists = MovieListSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuarios
        fields = ['id', 'username', 'email', 'password', 'avatar', 'country', 'date_added', 'movie_lists']

    def create(self, validated_data):
        user = Usuarios.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            avatar=validated_data['avatar'],
            country=validated_data['country'],
        )
        return user
