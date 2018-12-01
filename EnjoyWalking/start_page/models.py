# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Point(models.Model):
    latitude = models.CharField(max_length=100) # shirota
    longtitude = models.CharField(max_length=100)# dolgota
    rating = models.FloatField()
    description = models.TextField()


# Create your models here.
class Points(models.Model):
    latitude_a = models.CharField(max_length=100, default='55.7217974') # shirota
    longtitude_a = models.CharField(max_length=100, default='37.6118358')# dolgota
    latitude_b = models.CharField(max_length=100, default='55.8416519')  # shirota
    longtitude_b = models.CharField(max_length=100, default='37.4626163')  # dolgota
    rating = models.FloatField()
    description = models.TextField()
