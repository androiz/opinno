from django.db import models
from filer.fields.image import FilerImageField


class Character(models.Model):
    name = models.CharField(
        max_length=200,
        null=False, blank=False
    )
    height = models.CharField(
        max_length=10,
        null=False, blank=True
    )
    mass = models.CharField(
        max_length=10,
        null=False, blank=False
    )

    # Relationship
    homeworld = models.ForeignKey(
        'Planet',
        null=True, blank=True,
        related_name='homeworld_people',
        on_delete=models.SET_NULL
    )

    starships = models.ManyToManyField(
        'Starship',
        blank=True,
        related_name='characters'
    )

    # Control
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False, blank=False
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False, blank=False
    )

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'

    def __str__(self):
        return self.name


class CharacterImage(models.Model):
    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE,
        null=False, blank=False,
        related_name='character_images'
    )
    image = FilerImageField(
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="character_images"
    )
