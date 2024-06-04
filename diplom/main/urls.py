from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('cources', views.cources, name='cources'),
    path('prices', views.prices, name='prices'),
    path('reiting', views.reiting, name='reiting'),
    path('contacts', views.contacts, name='contacts'),
    path('forma', views.forma, name='forma'),
]