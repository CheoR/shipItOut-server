"""Container model"""

from django.db import models


class Container(models.Model):
    """
        Container model.
    """
    container = models.CharField(max_length=50)
    equipment_size = models.CharField(max_length=7)
    container_status = models.ForeignKey(
        "CntrStatus", on_delete=models.DO_NOTHING)
    is_damaged = models.BooleanField()
    is_need_inspection = models.BooleanField()
    is_overweight = models.BooleanField()
    is_in_use = models.BooleanField()
    notes = models.TextField(default='', blank=True)

    def __str__(self):
        return F"Container: {self.container}"
