# Generated by Django 4.2 on 2023-05-07 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_movie_user_delete_job_delete_person_movie_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='user',
        ),
        migrations.AddField(
            model_name='movie',
            name='isViewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_lists', to='miapp.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_lists', to='miapp.user')),
            ],
        ),
    ]
