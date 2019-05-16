from django.shortcuts import render, redirect, get_object_or_404

from .models import Movie, Rating
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/list.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # movie = Movie.objects.annotate(score_avg=Avg('score_avg')).get(pk=movie_pk)
    # ratings = movie.rating_set.all()
    ratings = movie.rating_set.annotate(score_avg=Avg('score')).filter(pk=movie_pk)
    context = {'movie': movie, 'ratings': ratings}
    return render(request, 'movies/detail.html', context)

def test(request):
    return render(request, 'movies/test.html')

@login_required
def new_rating(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    new_rating = Rating()
    new_rating.comment = request.POST.get('comment')
    context = {'movie': movie, 'ratings': ratings}
    new_rating.movie = movie
    new_rating.user = request.user
    new_rating.save()
    return redirect('movies:detail', movie_pk)

def delete_rating(request, movie_pk, rating_pk):
    rating = get_object_or_404(Rating, pk=rating_pk)
    rating.delete()
    return redirect('movies:detail', movie_pk)