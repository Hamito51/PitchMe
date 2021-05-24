from django.contrib.auth import get_user_model
from rest_framework import serializers
from social_core.tests.models import User

from accounts.services import sign_up


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'password',
            'email',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = sign_up(**validated_data)
        return user

