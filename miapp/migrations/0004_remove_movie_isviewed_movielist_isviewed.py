# Generated by Django 4.2 on 2023-05-19 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_rename_name_movie_title_remove_movie_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='isViewed',
        ),
        migrations.AddField(
            model_name='movielist',
            name='isViewed',
            field=models.BooleanField(default=False),
        ),
    ]
