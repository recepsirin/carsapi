from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework import generics, mixins
from .serializers import CarSerializers
from carsapp.models import cars


class CarsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    queryset = cars.objects.all()
    serializer_class = CarSerializers

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['year', 'brand', 'extcolor', 'intcolor', 'transmission']

    # def get_queryset(self):
    #     qs = cars.objects.all()
    #     year = self.request.query_params.get('year', None)
    #     if year is not None:
    #         qs = qs.filter(year=year)
    #     return qs

    def get_queryset(self):
        qs = cars.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(year=query) |
                Q(brand=query) |
                Q(extcolor=query) |
                Q(intcolor=query) |
                Q(transmission=query)
            )
        return qs

    # def get_queryset(self):
    #     return cars.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class CarsAPIRudView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = CarSerializers

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['year', 'brand', 'extcolor', 'intcolor', 'transmission']

    # def get_queryset(self):
    #     qs = cars.objects.all()
    #     year = self.request.query_params.get('year', None)
    #     if year is not None:
    #         qs = qs.filter(year=year)
    #     return qs

    def get_queryset(self):
        return cars.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}
