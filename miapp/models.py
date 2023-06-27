from django.db import models

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=60)
    email = models.CharField(max_length=50,unique=True)  # Campo único
    avatar = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    date_added = models.DateTimeField()

class ListaDePeliculas(models.Model):
    id = models.AutoField(primary_key=True)
    is_viewed = models.BooleanField()
    is_erased = models.BooleanField()
    date_added = models.DateTimeField()
    user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    movie = models.ForeignKey('Peliculas', on_delete=models.CASCADE)

class Peliculas(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    year = models.IntegerField()
    language = models.CharField(max_length=2)
    genre_name = models.CharField(max_length=20)
    genre_id = models.IntegerField()
    img_url = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
