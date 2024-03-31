from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def new_songs(request):
    return render(request, 'for_songs/new_songs.html')


def famous_songs(request):
    return render(request, 'for_songs/famous_songs.html')


def authors(request):
    return render(request, 'for_songs/authors.html')