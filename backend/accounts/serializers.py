from django.contrib.auth import get_user_model
from rest_framework import serializers
from social_core.tests.models import User

from accounts.services import sign_up


class UserSerializer(serializers.ModelSerializer):
    # # coordinates = serializers.CharField(read_only=True)
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    # patronymic = serializers.CharField()
    # birthday = serializers.DateField()

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'password',
            'email',
            # 'first_name',
            # 'last_name',
            # 'patronymic',
            # 'birthday'

        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = sign_up(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)