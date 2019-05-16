from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.list, name='list'),
    path('search/', views.search, name='search'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/new_rating/', views.new_rating, name='new_rating'),
    path('<int:movie_pk>/ratings/<int:rating_pk>/delete/', views.delete_rating, name='delete_rating'),
    path('test/', views.test),
]