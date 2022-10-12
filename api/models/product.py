"""Product model"""

from django.db import models


class Product(models.Model):
    """
        Product model.
    """

    product = models.CharField(max_length=50)
    weight = models.FloatField()
    is_fragile = models.BooleanField(default=False)
    is_damaged = models.BooleanField(default=False)
    is_reefer = models.BooleanField(default=False)
    is_haz = models.BooleanField(default=False)

    container = models.ForeignKey("Container", on_delete=models.SET_NULL, null=True, blank=True, related_name="products")

    def __str__(self):
        return F"container: {self.container} - {self.commodity}"
