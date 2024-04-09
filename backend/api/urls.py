from django.urls import path
from . import views

urlpatterns = [
    path('auth/token/login/', views.LoginView.as_view(), name='login'),
    path('users/', views.RegistrationView.as_view(), name='register_user'),
    path('users/<str:pk>/', views.UserProfileView.as_view(), name='user_profile'),
    path('auth/token/logout/', views.LogoutView.as_view(), name='logout'),
]
