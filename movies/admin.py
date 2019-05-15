from django.contrib import admin

# from .models import Movie, Genre, Cast, Crew, Rating
from .models import Movie, Genre, Cast, Crew
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_date', 'runtime', 'poster_path', 'overview', 'get_genres', 'get_crews', 'get_casts', 'get_similar']

    def get_genres(self, obj):
        if obj.genre: return list(obj.genre.values_list())
        else: return 'None'

    def get_crews(self, obj):
        if obj.crew: return list(obj.crew.values_list())
        else: return 'None'
    
    def get_casts(self, obj):
        if obj.cast: return list(obj.cast.values_list())
        else: return 'None'

    def get_similar(self, obj):
        if obj.similar_movie: return list(obj.similar_movie.values_list('id', flat=True))
        else: return 'None'

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
