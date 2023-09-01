from django.urls import path

from user.api.auth_views import (
    LogOutAPIView,
    LoginAPIView,
    SignUpAPIView,
)
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("signup/", SignUpAPIView.as_view(), name="signup"),
    path("logout/", LogOutAPIView.as_view(), name="logout"),
    path("refresh/", jwt_views.TokenRefreshView.as_view(), name="token-refresh"),
]
