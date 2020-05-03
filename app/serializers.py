from rest_framework.serializers import ModelSerializer
from .validators import *
from .models import *


class CenterSerializer(ModelSerializer):
    class Meta:
        model = Centers
        fields = ('center_name',)


class EntrySerializer(ModelSerializer):
    class Meta:
        model = Entries
        fields = (
            'name',
            'mobile',
            'address',
            'landmark',
            'center',
            'remark',
            'closed',
            'date_received',
            'date_closed'
        )
        # extra_kwargs = {
        #     'mobile': {
        #         'validators': [
        #             numeric_mobile_validator,
        #             mobile_length_validator
        #         ]
        #     }
        # }