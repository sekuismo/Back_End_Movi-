from django.db import models

class User(models.Model):

    name = models.CharField(max_length=100)
    password = models.CharField(max_length=60,default='')
    email= models.CharField(max_length=50)
    avatar = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

#es importante que el  parámetro related_name se llame de la misma forma que la instancia de la serialización de 
# la llave foránea 

class Movie(models.Model):

    title= models.CharField(max_length=50)
    description = models.CharField(max_length = 800)
    # year = models.CharField()
    language= models.CharField(max_length=2)
    genre_name= models.CharField(max_length=20)
    # genre_id= models.CharField()
    url= models.CharField(max_length=100,default='' )
    img_url = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
    # para funcion de eliminar pelicula se agrega el atributo boolean para ver si se elimino o no
    #El ISVIEWED debe estar en la entidad débil MovieList.
class MovieList(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_lists')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_lists')
    is_viewed = models.BooleanField(default=False)
    is_erased = models.BooleanField(default=False)
    def __str__(self):
        return f" {self.movie.title} {self.is_viewed}"
