from rest_framework import serializers
from carsapp.models import cars


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = cars
        fields = [
            'id',
            'year',
            'brand',
            'extcolor',
            'intcolor',
            'transmission',
            'price',
            'phone',
        ]
        read_only_fields = ['id']

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)
