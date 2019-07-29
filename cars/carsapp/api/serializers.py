from rest_framework import serializers
from cars.carsapp.models import cars


class BlogPostSerializers(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

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
