from django.db import models
from filer.fields.image import FilerImageField


class Film(models.Model):
    episode_id = models.IntegerField()
    title = models.CharField(
        max_length=200,
        null=False, blank=False
    )
    opening_crawl = models.TextField(
        null=False, blank=True
    )
    director = models.CharField(
        max_length=100,
        null=False, blank=False
    )

    # Relations
    characters = models.ManyToManyField(
        'Character', blank=True,
        related_name='films'
    )
    starships = models.ManyToManyField(
        'Starship', blank=True,
        related_name='films'
    )
    planets = models.ManyToManyField(
        'Planet', blank=True,
        related_name='films'
    )
    image = FilerImageField(
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="films"
    )

    # Relationship
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False, blank=False
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False, blank=False
    )

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return self.title
