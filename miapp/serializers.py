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

    class Meta:
        model = Usuarios
        fields = ['id', 'name', 'email', 'avatar', 'country', 'date_added', 'movie_lists']
