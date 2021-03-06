# Generated by Django 3.0.2 on 2020-02-05 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_playlist_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='userplaylists',
            name='playlist',
        ),
        migrations.DeleteModel(
            name='Playlist',
        ),
        migrations.AddField(
            model_name='playlists',
            name='UserPlaylist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.UserPlaylists'),
        ),
        migrations.AddField(
            model_name='playlists',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Song'),
        ),
    ]
