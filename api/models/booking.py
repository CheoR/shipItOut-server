"""Booking model"""

from django.db import models
from django.utils import timezone
from django.db.models import Count


def _pickup_appt():
    return timezone.now() + timezone.timedelta(days=7)

def _port_cut():
    return timezone.now() + timezone.timedelta(days=21)

def _delivery_appt():
    return timezone.now() + timezone.timedelta(days=60)


class Booking(models.Model):
    """
        Booking model.
    """ 

    ERROR = -1
    XX = 0
    PENDING = 1
    COMPLETE = 2
    CLOSED = 3
    
    BOOKING_STATUS_CHOICES = [
        ( ERROR, 'ERROR' ),
        ( XX, 'XX' ),
        ( PENDING, 'PENDING' ),
        ( COMPLETE, 'COMPLETE' ),
        ( CLOSED, 'CLOSED' ),
    ]

    # TODO: move auto-increment generator from frontent to backend for booking
    # check bookingViewSet for possible solution
    booking = models.CharField(max_length=12, default="")

    # since materials may be picked up at one address,
    # but not loaded into a container for shipment,
    # until it reaches another address, e.g. rail, warehouse
    unloading_destination_address = models.CharField(max_length=80, default="")
    loading_origin_address = models.CharField(max_length=80, default="")

    pickup_address = models.CharField(max_length=80, default="")
    pickup_appt = models.DateTimeField(default=_pickup_appt)

    rail_cutoff = models.DateTimeField(blank=True, null=True)
    port_cutoff = models.DateTimeField(default=_port_cut)

    delivery_address = models.CharField(max_length=80, default="")
    delivery_appt = models.DateTimeField(default=_delivery_appt)
    
    booking_status = models.IntegerField(
        choices=BOOKING_STATUS_CHOICES,
        default=XX,
    )

    are_documents_ready = models.BooleanField(default=False)
    are_dues_paid = models.BooleanField(default=False)

    # TODO: use annotate to dynamically calcuate if associated bookings, container, products have issues
    # docs, dues, booking status, container/product damage, container overweight, container needs inspection
    has_issue = models.BooleanField(default=False)

    booking_notes = models.TextField(default="", blank=True, )

    agent = models.ForeignKey("AppUser", on_delete=models.SET_NULL, null=True, blank=True, related_name="agent_bookings")
    carrier = models.ForeignKey("AppUser", on_delete=models.SET_NULL, null=True, blank=True, related_name="carrier_bookings")
    voyage = models.ForeignKey("Voyage", on_delete=models.SET_NULL, null=True, blank=True, related_name="voyage_bookings")
    loading_port = models.ForeignKey("Port", on_delete=models.SET_NULL, null=True, blank=True, related_name="loading_port_bookings")
    unloading_port = models.ForeignKey("Port", on_delete=models.SET_NULL, null=True, blank=True, related_name="unloading_port_bookings")

    @property
    def container_count(self):
        return self.containers.count()
    
    @property
    def product_count(self):
        _count = 0
        for container in self.containers.all():
            _count += container.products.count()
        return _count
