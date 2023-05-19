from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=40,default='')
    email= models.CharField(max_length=50)
    avatar = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#es importante que el  parámetro related_name se llame de la misma forma que la instancia de la serialización de 
# la llave foránea 

class Movie(models.Model):
    title=models.CharField(max_length=30)
    description = models.CharField(max_length = 1000)
    url= models.CharField(max_length=100,default='' )
    isViewed = models.BooleanField(default=False)
    image = models.CharField(max_length=60)
    def __str__(self):
        return self.title
    

    #El ISVIEWED debe estar en la entidad débil MovieList.
class MovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_lists')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_lists')
    def __str__(self):
        return f" {self.movie.title}"