"""Voyage model"""

from django.db import models


class Voyage(models.Model):
    """
        Voyage model.
    """
    voyage = models.CharField(max_length=10)
    vessel = models.ForeignKey("Vessel", on_delete=models.DO_NOTHING)
