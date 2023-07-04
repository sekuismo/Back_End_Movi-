from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
admin.site.register(models.Usuarios,UserAdmin)
admin.site.register(models.Peliculas)
admin.site.register(models.ListaDePeliculas)