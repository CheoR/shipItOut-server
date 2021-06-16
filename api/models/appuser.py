"""AppUser Model"""

from django.contrib.auth.models import User
from django.db import models


class AppUser(models.Model):
    """
        AppUser user model add fields to the default User model.
    """

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
