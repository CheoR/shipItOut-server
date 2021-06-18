"""BkgStatus Serializer"""

from rest_framework import serializers

from api.models import BkgStatus


class BkgStatusSerializer(serializers.ModelSerializer):
    """JSON serializer for BkgStatus"""

    class Meta:
        model = BkgStatus
        fields = ('id', 'status')
