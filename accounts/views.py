from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.conf import settings

from .forms import UserCustomCreationForm, AuthenticationForm, ProfileForm
from .models import Profile

from django.http import JsonResponse, HttpResponseBadRequest

# Create your views here.
def list(request):
    User = get_user_model()
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'accounts/list.html', context)
    
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:list')
    if request.method == "POST":
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user_login(request, user)
            return redirect('accounts:list')
    else:    
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)
    
    
def login(request):
    if request.method == "POST":
        signin_form = AuthenticationForm(request, request.POST)
        if signin_form.is_valid():
            user_login(request, signin_form.get_user())
            return redirect('accounts:list')
    signin_form = AuthenticationForm()
    context = {'form': signin_form}
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    user_logout(request)
    return redirect('accounts:list')

@login_required
def profile(request):
    user = get_user_model()
    context = {'user_info': user}
    return render(request, 'accounts/profile.html', context)

@login_required
def profile_update(request):
    try :
        request.user.profile
    except:
        Profile.objects.create(user=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:profile')
    profile_form = ProfileForm(instance=request.user.profile)
    context = {'profile_form': profile_form}
    return render(request, 'accounts/profile_update.html', context)