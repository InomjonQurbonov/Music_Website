from django.urls import path
from .views import UploadMusicView

urlpatterns = [
    path('upload-music/', UploadMusicView.as_view(), name=  'add_song'),
]
