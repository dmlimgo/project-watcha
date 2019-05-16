from django.shortcuts import render, redirect, get_object_or_404

from .models import Movie, Rating
from .forms import RatingForm
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/list.html', context)
    
def search(request):
    # pass
    movies = Movie.objects.all()
    keyword = request.POST.get('search')
    results = []
    for movie in movies.filter(title__contains=keyword):
        results.append(movie)
    print(results)
    context = {
        'keyword': keyword,
        'results': results
    }
    return render(request, 'movies/search.html', context)

@login_required
def detail(request, movie_pk):
    # movie = get_object_or_404(Movie, pk=movie_pk)
    movie = Movie.objects.annotate(score_avg=Avg('rating__score')).get(pk=movie_pk)
    ratings = movie.rating_set.all()
    # ratings = movie.rating_set.annotate(score_avg=Avg('score')).filter(pk=movie_pk)
    if request.method == "POST":
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.user = request.user
            rating.save()
            return redirect('movies:detail', movie.pk)
    else:
        rating_form = RatingForm()
    context = {
        'movie': movie,
        'ratings': ratings,
        'rating_form': rating_form
    }
    return render(request, 'movies/detail.html', context)

@login_required
def new_rating(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    new_rating = Rating()
    new_rating.comment = request.POST.get('comment')
    new_rating.score = request.POST.get('score')
    new_rating.movie = movie
    new_rating.user = request.user
    new_rating.save()
    return redirect('movies:detail', movie_pk)

@login_required
def delete_rating(request, movie_pk, rating_pk):
    rating = get_object_or_404(Rating, pk=rating_pk)
    rating.delete()
    return redirect('movies:detail', movie_pk)
    
    
def test(request):
    return render(request, 'movies/test.html')