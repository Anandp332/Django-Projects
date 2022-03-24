from django.db import models


# Example of One to Many/ Many to One relation
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=10)
    year = models.IntegerField()
    ratings = models.FloatField()

    def __str__(self):
        return self.name


class AudioSongs(models.Model):
    name = models.CharField(max_length=10)
    length = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
