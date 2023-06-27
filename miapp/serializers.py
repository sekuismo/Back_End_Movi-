from rest_framework import serializers
from .models import Usuarios,Peliculas,ListaDePeliculas


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peliculas
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    movie_lists = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Usuarios
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = ListaDePeliculas
        fields = '__all__'
