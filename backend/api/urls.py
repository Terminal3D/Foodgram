from django.urls import path
from . import views

urlpatterns = [
    path('auth/token/login/', views.LoginView.as_view(), name='login'),
    path('auth/token/logout/', views.LogoutView.as_view(), name='logout'),
    path('users/', views.RegistrationView.as_view(), name='register_user'),
    path('users/set_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('users/<str:pk>/', views.UserProfileView.as_view(), name='user_profile'),
]
