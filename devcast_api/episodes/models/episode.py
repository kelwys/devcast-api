from django.db import models


class Episode(models.Model):
    title = models.CharField('Titulo', max_length=150)
    members = models.CharField('Membros', max_length=255)
    published_at = models.DateField('Data de publicação')
    thumbnail = models.URLField()
    description = models.TextField('Descrição')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Episodio"
        verbose_name_plural = "Episodios"
