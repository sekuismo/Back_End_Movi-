from django.db import models
from django.contrib.auth.models import AbstractUser

# POSTGRES PORT 5432
class Usuarios(AbstractUser):
    avatar = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class ListaDePeliculas(models.Model):
    id = models.AutoField(primary_key=True)
    is_viewed = models.BooleanField(default=False)  
    is_erased = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='movie_lists')
    movie = models.ForeignKey('Peliculas', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.movie} - {self.user}'


class Peliculas(models.Model):
    movie_id = models.IntegerField(primary_key=True,default=0)   #este será el campo único que vendrá desde la API
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    year = models.IntegerField()
    language = models.CharField(max_length=2)
    genre_name = models.CharField(max_length=20)
    genre_id = models.IntegerField()
    img_url = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'
