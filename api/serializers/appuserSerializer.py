"""AppUser Serialzier"""

from rest_framework import serializers

from api.models import AppUser


class DefaultAppUserSerializer(serializers.ModelSerializer):
    """JSON serializer for AppUsers
        "id": 1, # appuser.id
        "company": "pug transport",
        "role": "ops",
        "phone": "615-123-4567",
        "account_type": 3,
        "user": 1 # user.id
    """
    
    class Meta:
        model = AppUser
        fields = '__all__'
        # fields = ('id', 'user', 'token', 'username', 'email', 'first_name',
        #           'last_name', 'company', 'role', 'phone', 'account_type')


class AppUserSerializer(serializers.ModelSerializer):
    """JSON serializer for AppUsers
            "id": 1,
        "company": "pug transport",
        "role": "ops",
        "phone": "615-123-4567",
        "account_type": 3,
        "user": {
            "id": 1,
            "password": "pbkdf2_sha256$320000$G15hzDVSKvdszzqFzB8mNw$GFBEHIMCyWmettBq7Q9P29HcrrL3awRTc52eisBVT1A=",
            "last_login": null,
            "is_superuser": false,
            "username": "peggypug",
            "first_name": "peggy",
            "last_name": "pug",
            "email": "peggy@pug.com",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2022-10-14T02:11:55.019760Z",
            "groups": [],
            "user_permissions": []
        }
    """
    
    class Meta:
        model = AppUser
        fields = '__all__'
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
