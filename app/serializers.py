from rest_framework.serializers import ModelSerializer
from .models import *


class CenterSerializer(ModelSerializer):
    class Meta:
        model = Centers
        fields = ('center_name',)