"""AppUser Model"""

from django.contrib.auth.models import User
from django.db import models


class AppUser(models.Model):
    """
        AppUser user model add fields to the default User model.
    """

    # ACCOUNT TYPES
    ERROR = -1
    DEFAULT = 0
    SHIPPER = 1
    BROKER = 2
    WAREHOUSE = 3
    CARRIER = 4
    PORTOPS = 5

    ACCOUNT_CHOICES = [
        ( ERROR, 'ERROR' ),
        ( DEFAULT, 'DEFAULT' ),
        ( SHIPPER, 'SHIPPER' ),
        ( BROKER, 'BROKER' ),
        ( WAREHOUSE, 'WAREHOUSE' ),
        ( CARRIER, 'CARRIER' ),
        ( PORTOPS, 'PORTOPS' ),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)

    account_type = models.IntegerField(
        choices=ACCOUNT_CHOICES,
        default=DEFAULT,
    )
