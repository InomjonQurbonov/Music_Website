from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SongsForm
from app_news.models import Songs


class UploadMusicView(CreateView):
    model = Songs
    form_class = SongsForm
    template_name = 'song/add_songs.html'
    success_url = reverse_lazy('index')
