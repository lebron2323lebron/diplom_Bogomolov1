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
    path('course1', views.course1, name='course1'),
    path('course2', views.course2, name='course2'),
    path('course3', views.course3, name='course3'),
    path('modules1', views.module, name='modules1'),
    path('modules11', views.module11, name='module11'),
    path('modules12', views.module12, name='module12'),
    path('modules13', views.module13, name='module13'),
    path('modules14', views.module14, name='module14'),
    path('add_reviews', views.add_reviews, name='add_reviews'),

    path('zapisi', views.schedule, name="zapisi"),
]