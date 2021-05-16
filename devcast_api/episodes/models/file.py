from django.db import models

from devcast_api.episodes.models import Episode


class File(models.Model):
    TYPE_CHOICES = (
        ('audio/x-m4a', 'x-m4a'),
        ('audio/mp3', 'mp3')
    )

    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='files')
    url = models.URLField()
    type = models.CharField('Tipo', choices=TYPE_CHOICES, max_length=25)
    duration = models.IntegerField('Duração')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"
