from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit/<int:pk>', views.ProfileUpdate.as_view(), name='profile_edit'),
]