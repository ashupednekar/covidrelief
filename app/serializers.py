from rest_framework.serializers import ModelSerializer
from .validators import *
from .models import *


class CenterSerializer(ModelSerializer):
    class Meta:
        model = Centers
        fields = ('center_name', 'stock_count')

class StockSerializer(ModelSerializer):
    class Meta:
        model = Stocks
        fields = ('count',)

class EntrySerializer(ModelSerializer):
    class Meta:
        model = Entries
        fields = (
            'ward',
            'actor',
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


class UploadSerializer(ModelSerializer):
    class Meta:
        model = Upload
        fields = ('fn', 'tomark')
