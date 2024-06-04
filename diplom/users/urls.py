from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views
from .views import ProfileUpdateView, UserRegisterView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), 
    path('<str:username>/', views.UserProfileView.as_view(), name='profile-detail'),
]