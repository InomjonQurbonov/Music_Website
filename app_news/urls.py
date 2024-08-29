from django.urls import path
from .views import IndexView, NewSongsView, FamousSongsView, AuthorsView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('new-songs/', NewSongsView.as_view(), name='new_songs'),
    path('famous-songs/', FamousSongsView.as_view(), name='famous_songs'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('contact/', ContactView.as_view(), name='contact'),
]
