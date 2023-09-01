from django.urls import path, include

urlpatterns = [
    path("auth/", include("user.routes.auth_routes"), name="main-auth"),
    path("profile/", include("user.routes.profile_routes"), name="main-profile"),
]
