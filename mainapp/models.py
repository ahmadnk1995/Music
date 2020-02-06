from django.db import models
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.conf import settings


class Song(models.Model):
    name = models.CharField(max_length=30)
    audio_track = models.FileField()

    def __unicode__(self):
        return self.songName

class UserPlaylists(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Playlists(models.Model):
    UserPlaylist = models.ForeignKey(UserPlaylists,
                             on_delete=models.CASCADE)
    song = models.ForeignKey(Song,
                             on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)



