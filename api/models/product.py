"""Product model"""

from django.db import models


class Product(models.Model):
    """
        Product model.
    """
    commodity = models.CharField(max_length=50)
    weight = models.FloatField()
    is_fragile = models.BooleanField()
    is_haz = models.BooleanField()
    is_damaged = models.BooleanField()
    is_reefer = models.BooleanField()
    container = models.ForeignKey("Container", on_delete=models.DO_NOTHING)

    def __str__(self):
        return F"{self.commodity} - container id: {self.container}"
