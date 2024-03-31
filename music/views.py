from django.shortcuts import render, redirect
from .forms import SongsForm


def upload_music(request):
    if request.method == 'POST':
        form = SongsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a page showing uploaded music
    else:
        form = SongsForm()
    return render(request, 'song/add_songs.html', {'form': form})
