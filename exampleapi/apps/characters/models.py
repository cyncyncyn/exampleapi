from __future__ import unicode_literals

from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=40)
    species = models.CharField(max_length=40)
    photos = models.ManyToManyField('Photo', blank='True')
    planet = models.ManyToManyField('Planet', blank='True')

class Photo(models.Model):
    name = models.CharField(max_length=40, blank='True')
    url = models.URLField(max_length=200)


class Planet(models.Model):
    name = models.CharField(max_length=40)
    climate = models.CharField(max_length=40)
    diameter = models.PositiveIntegerField()
    population = models.PositiveIntegerField(blank='True')
