from django.db import models


class Songs(models.Model):
    song_name = models.CharField(max_length=250, verbose_name='Song Name')
    song_author = models.CharField(max_length=250, verbose_name='Song Author')
    song_description = models.TextField(verbose_name='Song Description')
    favorite_song = models.BooleanField(default=False, verbose_name='Favourite Songs')
    song_img = models.ImageField(upload_to='song_img/', verbose_name='Song Image', default='default.jpg')
    song_file = models.FileField(upload_to='songs/', verbose_name='Song File')
    song_listen_count = models.IntegerField(default=0, verbose_name='Song Listen Count')
    song_add_date = models.DateTimeField(auto_now_add=True, verbose_name='Song Added Date')

    def __str__(self):
        return self.song_name

    class Meta:
        db_table = 'songs'
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'
        ordering = ['-song_add_date']
