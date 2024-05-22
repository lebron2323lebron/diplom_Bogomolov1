from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('float', views.float, name='float'),
    path('prices', views.prices, name='prices'),
]