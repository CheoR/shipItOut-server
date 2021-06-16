"""Carrier model"""

from django.db import models


class Carrier(models.Model):
    """
        Carrier model.
    """
    name = models.CharField(max_length=50)
