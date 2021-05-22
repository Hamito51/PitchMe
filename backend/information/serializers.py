from rest_framework import serializers

from information.models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = [
            'city',
            'street_type',
            'street',
            'house',
            'flat'
        ]