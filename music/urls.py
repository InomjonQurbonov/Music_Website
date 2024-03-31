from django.urls import path
from .views import upload_music

urlpatterns = [
    path('add_song', upload_music, name='add_song')
]