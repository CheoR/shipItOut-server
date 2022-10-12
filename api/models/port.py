"""Port model"""

from django.db import models


class Port(models.Model):
    """
        Port model.
    """

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
