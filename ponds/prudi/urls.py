from django.urls import path
from .views import Demo, HomePage, Proekti

urlpatterns = [
    path('', HomePage.as_view(), name='base'),
    path('projects/', Proekti.as_view(), name='proekti'),
    path('demo/', Demo.as_view(), name='demo'),
]