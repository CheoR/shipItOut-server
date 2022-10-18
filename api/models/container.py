"""Container model"""

from django.db import models


class Container(models.Model):
    """
        Container model.
    """

    ERROR = -1
    XX00 = 0
    OG40 = 1
    ST20 = 2
    ST40 = 3
    HC20 = 4
    HC40 = 5

    YARD = 6
    RAIL = 7
    SAIL = 8
    PORT = 9
    BERTH = 10
    PICKUP = 11
    TRANSIT = 12
    STORAGE = 13
    DELIVERY = 14
    WAREHOUSE = 15
    INSPECTION = 16

    EQUIPMENT_CHOICES = [
        ( XX00, '' ),
        ( OG40, '40OG' ),
        ( ST20, '20ST' ),
        ( ST40, '40ST' ),
        ( HC20, '20HC' ),
        ( HC40, '40HC' ),
    ]

    LOCATION_CHOICES = [
        ( YARD, 'YARD' ),
        ( RAIL, 'RAIL' ),
        ( SAIL, 'SAIL' ),
        ( PORT, 'PORT' ),
        ( BERTH, 'BERTH' ),
        ( PICKUP, 'PICKUP' ),
        ( TRANSIT, 'TRANSIT' ),
        ( STORAGE, 'STORAGE' ),
        ( DELIVERY, 'DELIVERY' ),
        ( WAREHOUSE, 'WAREHOUSE' ),
        ( INSPECTION, 'INSPECTION' ),
    ]

    container = models.CharField(max_length=8)
    container_type = models.IntegerField(
        choices=EQUIPMENT_CHOICES,
        default=XX00,
    )

    container_location = models.IntegerField(
        choices=LOCATION_CHOICES,
        default=YARD,
    )

    booking = models.ForeignKey("Booking", on_delete=models.SET_NULL, null=True, blank=True, related_name="containers")

    is_needs_inspection = models.BooleanField(default=False)
    # TODO: make property, calculate using annotate to dynamically calcuate if container is overweight
    is_overweight = models.BooleanField(default=False)
    is_container_damaged = models.BooleanField(default=False)
    # TODO: make property, calculate using annotate to dynamically calcuate if associated to a booking
    is_in_use = models.BooleanField(default=False)
    container_notes = models.TextField(default="", blank=True, )

    @property
    def product_count(self):
        return self.products.count()
