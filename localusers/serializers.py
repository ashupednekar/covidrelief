from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import *


class LocalUserSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(LocalUserSerializer, self).__init__(*args, **kwargs)
        if self.context['request'].method == "PUT":
            self.fields.pop('password')

    class Meta:
        model = LocalUser
        fields = ('id', 'username', 'full_name', 'status', 'disabled', 'disabled', 'email', 'password', 'center', 'role', 'is_superuser')
