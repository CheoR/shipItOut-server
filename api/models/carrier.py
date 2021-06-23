"""Carrier model"""

from django.db import models


class Carrier(models.Model):
    """
        Carrier model.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return F"{self.name}"
