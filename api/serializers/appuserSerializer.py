"""AppUser Serialzier"""

from rest_framework import serializers

from api.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    """JSON serializer for AppUsers"""

    class Meta:
        model = AppUser
        fields = ('id', 'user', 'company', 'role', 'phone')
