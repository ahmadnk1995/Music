# Generated by Django 3.0.2 on 2020-02-05 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200206_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='name',
        ),
    ]
