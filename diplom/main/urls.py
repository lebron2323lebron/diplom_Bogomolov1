from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('cources', views.cources, name='cources'),
    path('prices', views.prices, name='prices'),
    path('reiting', views.reiting, name='reiting'),
    path('contacts', views.contacts, name='contacts'),
    path('forma', views.ApplicationFormView.as_view(), name='forma'),
    path("profile", views.profile, name="profile"),
    path("profile-courses", views.profile_courses, name="profile-courses"),
    path("about", views.about, name="about"),
]