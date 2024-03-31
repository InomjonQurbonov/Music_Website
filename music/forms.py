from django import forms
from app_news.models import Songs


class SongsForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = ['song_name', 'song_author', 'song_description', 'song_img', 'song_file']

    def __init__(self, *args, **kwargs):
        super(SongsForm, self).__init__(*args, **kwargs)
        self.fields['song_description'].widget.attrs['rows'] = 4  # Adjust rows for the song description field
