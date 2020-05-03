from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import *


class LocalUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocalUser
        fields = ('id', 'username', 'full_name', 'language', 'flag', 'no_of_concats', 'type', 'role', 'skills', 'group', 'status', 'disabled', 'filename', 'disabled', 'email', 'password')