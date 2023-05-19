from rest_framework import serializers
from .models import User,Movie,MovieList


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    movie_lists = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = MovieList
        fields = '__all__'
