"""Service model"""

from django.db import models


class Service(models.Model):
    """
        Service model with name of ship service.
    """
    name = models.CharField(max_length=5)
