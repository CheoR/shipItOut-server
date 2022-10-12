"""Voyage model"""

from django.db import models


class Voyage(models.Model):
    """
        Voyage model.
    """
    
    XX = 0
    WC = 1
    EC = 2
    NE = 3
    SE = 4
    GU = 5
    
    SERVICE_CHOICES = [
        ( XX, '' ),
        ( WC, 'WC' ),
        ( EC, 'EC' ),
        ( NE, 'NE' ),
        ( SE, 'SE' ),
        ( GU, 'GU' ),
    ]
    
    voyage = models.CharField(max_length=10)
    service = models.IntegerField(
        choices=SERVICE_CHOICES,
        default=XX,
    )

    # no need to add _id,
    # django add it in for you
    vessel = models.ForeignKey("Vessel", on_delete=models.SET_NULL, null=True, blank=True, related_name="voyages")
