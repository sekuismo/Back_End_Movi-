# Generated by Django 4.2 on 2023-06-29 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0010_alter_usuarios_options_alter_usuarios_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]