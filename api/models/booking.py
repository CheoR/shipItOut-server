"""Booking model"""

from django.db import models


class Booking(models.Model):
    """
        Booking model.
    """
    user = models.ForeignKey("AppUser", on_delete=models.DO_NOTHING)
    booking = models.CharField(max_length=50)
    voyage_reference = models.ForeignKey("Voyage", on_delete=models.DO_NOTHING)
    container = models.ForeignKey("Container", on_delete=models.DO_NOTHING)
    carrier = models.ForeignKey("Carrier", on_delete=models.DO_NOTHING)
    loading_origin = models.CharField(max_length=50)
    unloading_destination = models.CharField(max_length=50)
    pickup_address = models.CharField(max_length=50)
    pickup_appt = models.DateTimeField()
    port = models.ForeignKey("Port", on_delete=models.DO_NOTHING)
    port_cutoff = models.DateTimeField()
    rail_cutoff = models.DateTimeField(blank=True, null=True)
    document = models.ForeignKey("Document", on_delete=models.DO_NOTHING)
    due = models.ForeignKey("Due", on_delete=models.DO_NOTHING)
    has_issue = models.BooleanField()
    booking_status = models.ForeignKey(
        "BkgStatus", on_delete=models.DO_NOTHING)
    notes = models.TextField(default='', blank=True)
