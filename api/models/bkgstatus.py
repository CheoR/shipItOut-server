"""BkgStatus model"""

from django.db import models


class BkgStatus(models.Model):
    """
        BkgStatus model.
    """
    status = models.CharField(max_length=25)
