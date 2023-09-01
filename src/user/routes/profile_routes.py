from django.urls import path
from user.api.profile_views import (
    PasswordChangeAPIView,
    ProfileAPIView,
)

urlpatterns = [
    path("", ProfileAPIView.as_view(), name="profile"),
    path("password/change/", PasswordChangeAPIView.as_view(), name="password-change"),
] 
