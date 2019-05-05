from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MoviesAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('id', 'title', 'date_created')

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MoviesAdmin)
