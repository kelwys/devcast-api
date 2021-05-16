from django.contrib import admin

from .models import Episode, File


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('url', 'duration')
