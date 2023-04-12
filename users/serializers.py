from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError


class UserValidate(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, password):
        pass
        return password


class UserLoginValidateSerializer(UserValidate):
    pass


class UserCreateValidateSerializer(UserValidate):

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise ValidationError('User already exists!')


class ConfirmCodeValidateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(min_length=6, max_length=6)
