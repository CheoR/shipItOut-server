"""AppUser Serialzier"""

from rest_framework import serializers

from api.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    """JSON serializer for AppUsers"""
    
    class Meta:
        model = AppUser
        fields = '__all__'
        # fields = ('id', 'user', 'token', 'username', 'email', 'first_name',
        #           'last_name', 'company', 'role', 'phone', 'account_type')
        depth = 5


class PartialAppUserSerializer(AppUserSerializer):
    """JSON serializer for AppUser with some fields excluded"""
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # token = serializers.PrimaryKeyRelatedField(read_only=True)

    first_name = serializers.CharField(source = "user.first_name")
    last_name = serializers.CharField(source = "user.last_name")
    username = serializers.CharField(source = "user.username")
    email = serializers.CharField(source = "user.email")
    
    account_type = serializers.SerializerMethodField()

    class Meta:
        model = AppUser
        exclude = ('id', 'user', )
        depth = 1
    
    def get_account_type(self, obj):
        """Turn Enum choice account_type selection from number into human-readble string."""
        return obj.get_account_type_display()

class AppUserCarrierSerializer(serializers.ModelSerializer):
    """JSON serializer for AppUsers"""
    
    class Meta:
        model = AppUser
        fields = ('id', 'company' )
