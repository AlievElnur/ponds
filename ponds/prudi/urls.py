from django.urls import path
from .views import HomePage, Proekti

urlpatterns = [
    path('', HomePage.as_view(), name='base'),
    path('projects/', Proekti.as_view(), name='proekti'),
]