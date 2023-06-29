from rest_framework import serializers
from .models import Usuarios, Peliculas, ListaDePeliculas

#serializadores para devolver los usuarios en json para que sean consumidos por el front end
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
        fields = ['id', 'name', 'password', 'email', 'avatar', 'country', 'date_added', 'movie_lists']

    # def create(self, validated_data):
    #     # Agregar lógica adicional si es necesario antes de crear el usuario
    #     user = Usuarios.objects.create(**validated_data)
    #     return user
