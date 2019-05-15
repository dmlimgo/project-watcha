from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Genre(models.Model):
    type = models.CharField(max_length=20)

    def __repr__(self):
        return f'{self.pk}: {self.type}'

class Cast(models.Model):
    name = models.CharField(max_length=50)

class Crew(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=30)
    runtime = models.IntegerField()
    poster_path = models.CharField(max_length=200)
    overview = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='movie')
    crew = models.ManyToManyField(Crew, related_name='movie')
    cast = models.ManyToManyField(Cast, related_name='movie')
    similar_movie = models.ManyToManyField('self', blank=True)

class Rating(models.Model):
    comment = models.TextField(blank=True)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)