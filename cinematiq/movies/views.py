from django.shortcuts import render
from .models import Movie
from django.contrib.auth.decorators import login_required

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': movies})

def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

def stream(request, movie_id):
    # Fetch the movie from the database
    movie = Movie.objects.get(pk=movie_id)

    # Pass the movie to the template
    return render(request, 'movies/stream.html', {'movie': movie})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
