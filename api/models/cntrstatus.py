"""CntrStatus model"""

from django.db import models


class CntrStatus(models.Model):
    """
        CntrStatus model.
    """
    status = models.CharField(max_length=25)
