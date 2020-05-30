from django.db import models


class RecentlyVisited(models.Model):
    session = models.CharField(
        max_length=100,
        null=False, blank=False
    )
    url = models.URLField(
        max_length=100,
        null=False, blank=False
    )

    # Control
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False, blank=False
    )

    def __str__(self):
        return self.url
