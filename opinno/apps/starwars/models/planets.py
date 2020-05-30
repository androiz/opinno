from django.db import models


class Planet(models.Model):
    name = models.CharField(
        max_length=200,
        null=False, blank=False
    )
    diameter = models.IntegerField(
        null=False, blank=True
    )
    terrain = models.CharField(
        max_length=100,
        null=False, blank=False
    )
    population = models.IntegerField(
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
        verbose_name = 'Planet'
        verbose_name_plural = 'Planets'

    def __str__(self):
        return self.name
