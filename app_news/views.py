from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class NewSongsView(TemplateView):
    template_name = 'for_songs/new_songs.html'


class FamousSongsView(TemplateView):
    template_name = 'for_songs/famous_songs.html'


class AuthorsView(TemplateView):
    template_name = 'for_songs/authors.html'


class ContactView(TemplateView):
    template_name = 'contact_us.html'