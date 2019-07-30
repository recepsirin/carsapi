from .views import CarsAPIView, CarsAPIRudView
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    url(r'^$', CarsAPIView.as_view(), name='cars-view'),
    url(r'^(?P<id>\d+)/$', CarsAPIRudView.as_view(), name='cars-rud')
]

