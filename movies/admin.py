from django.contrib import admin

from .models import Movie, Genre, Cast, Crew #, Rating
# from .models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_date', 'runtime', 'poster_path', 'overview']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    
class CastAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class CrewAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ['id', 'comment', 'score', 'movie', 'user']
    
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(Crew, CrewAdmin)
# admin.site.register(Rating, RatingAdmin)
