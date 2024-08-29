from django.contrib import admin
from .models import Songs, Contact


class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'song_name', 'song_listen_count', 'song_author']
    search_fields = ['song_name', 'song_author', 'song_description', 'song_add_date']
    list_filter = ['song_name', 'song_author', 'song_listen_count', 'song_add_date']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email']
    search_fields = ['full_name', 'email', 'message']
    list_filter = ['full_name', 'email']


admin.site.register(Songs, SongAdmin)
admin.site.register(Contact, ContactAdmin)
