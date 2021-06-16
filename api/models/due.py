"""Due model"""

from django.db import models


class Due(models.Model):
    """
        Due model.
    """
    are_dues_paid = models.BooleanField()
