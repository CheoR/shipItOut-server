"""Default AppUser Serialzier"""

from rest_framework import serializers

from api.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    """JSON serializer for AppUsers"""
    
    class Meta:
        model = AppUser
        fields = '__all__'
        # fields = ('id', 'user', 'token', 'username', 'email', 'first_name',
        #           'last_name', 'company', 'role', 'phone', 'account_type')
