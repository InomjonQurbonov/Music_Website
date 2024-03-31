from django.urls import path

from .views import (
    index, new_songs,
    famous_songs, authors
)

urlpatterns = [
    path('', index, name='index'),
    path('new_songs/', new_songs, name='new_songs'),
    path('famous_songs/', famous_songs, name='famous_songs'),
    path('authors/', authors, name='authors'),
]