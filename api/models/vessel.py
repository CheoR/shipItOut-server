"""Vessel model"""

from django.db import models


class Vessel(models.Model):
    """
        Vessel model with name of vessel.
    """
    name = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    # no need to add _id,
    # django add it in for you
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
