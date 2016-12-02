from __future__ import unicode_literals

from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=40)
    species = models.CharField(max_length=40)
    photo_url = models.URLField(max_length=255, blank=True)
