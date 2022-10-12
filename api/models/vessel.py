"""Vessel model"""

from django.db import models


class Vessel(models.Model):
    """
        Vessel model with name of vessel.
    """

    name = models.CharField(max_length=50)
