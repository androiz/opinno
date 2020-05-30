from django.db import models


class Starship(models.Model):
    name = models.CharField(
        max_length=200,
        null=False, blank=False
    )
    model = models.CharField(
        max_length=200,
        null=False, blank=True
    )
    length = models.IntegerField(
        null=False, blank=False
    )
    crew = models.CharField(
        max_length=15,
        null=False, blank=False
    )
    cargo_capability = models.IntegerField(
        null=False, blank=False
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
        verbose_name = 'Starship'
        verbose_name_plural = 'Starships'

    def __str__(self):
        return self.name
