from django.contrib import admin

from mainapp.models import Song , Playlists , UserPlaylists

admin.site.register(Song)
admin.site.register(Playlists)
admin.site.register(UserPlaylists)