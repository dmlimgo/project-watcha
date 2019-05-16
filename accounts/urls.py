from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.list, name='list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:user_pk>/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]