"""Due Serializer"""

from rest_framework import serializers

from api.models import Due


class DueSerializer(serializers.ModelSerializer):
    """JSON serializer for Dues"""

    class Meta:
        model = Due
        fields = ('id', 'are_dues_paid')
