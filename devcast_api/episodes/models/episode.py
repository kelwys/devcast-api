from django.db import models

from devcast_api.episodes.models.file import File


class Episode(models.Model):
    title = models.CharField('Titulo', max_length=150)
    members = models.CharField('Membros', max_length=255)
    published_at = models.DateField('Data de publicação')
    thumbnail = models.URLField()
    description = models.TextField('Descrição')
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='episode')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Episodio"
        verbose_name_plural = "Episodios"
