from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='base'),
    path('demo/', Demo.as_view(), name='demo'),
    path('fish/', FishOpen.as_view(), name='fish'),
    path('sculptures/', SculpturesOpen.as_view(), name='sculptures'),
    path('chanel/', ChannelsOpen.as_view(), name='chanel'),
    path('plants/', PlantsOpen.as_view(), name='plants'),
    path('other/', OtherOpen.as_view(), name='other'),
    path('', contact_view, name='contact'),
]