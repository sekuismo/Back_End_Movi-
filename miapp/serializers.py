from rest_framework import serializers
from .models import Usuarios, Peliculas, ListaDePeliculas

#serializadores para devolver los usuarios en json para que sean consumidos por el front end
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peliculas
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    movie_id = serializers.IntegerField(required=True)

    class Meta:
        model = ListaDePeliculas
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    movie_lists = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Usuarios
        fields = ['id', 'username','email', 'avatar', 'country', 'date_added', 'movie_lists', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password') #elimina la contraseña para que no se represente en el Json
        return representation
