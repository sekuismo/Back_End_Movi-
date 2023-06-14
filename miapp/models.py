from django.db import models



class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=60)
    email = models.CharField(max_length=50,unique=True)#campo único
    avatar = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    date_added = models.DateTimeField()
    def __str__(self):
        return self.name


class ListaDePeliculas(models.Model):
    id = models.AutoField(primary_key=True)
    is_viewed = models.BooleanField()
    is_erased = models.BooleanField()
    date_added = models.DateTimeField()
    user = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    movie = models.ForeignKey('Peliculas',on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user} : {self.movie}'

class Peliculas(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    year = models.IntegerField()
    language = models.CharField(max_length=2)
    genre_name = models.CharField(max_length=100)
    genre_id = models.IntegerField()
    img_url = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    

    #El ISVIEWED debe estar en la entidad débil MovieList.
