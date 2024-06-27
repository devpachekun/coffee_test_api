from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)
from . import views

# Custom Access Token
from .views import MyTokenObtainPairView

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='api-token-auth'),
    path('refresh-token/', TokenRefreshView.as_view(), name='api-token-refresh'),
    path('user-transaction/', views.UserTransactionView.as_view(), name='user-transaction'),
    path('get-coffees/', views.PublicCoffeesView.as_view(), name='public-get-coffees'),
    path('admin/coffees/', views.CoffeesView.as_view(), name='admin-coffees'),
    path('admin/coffees/<int:pk>/', views.CoffeesView.as_view(), name='coffees-detail'),
    path('admin/users/', views.UsersView.as_view(), name='users-detail')
]