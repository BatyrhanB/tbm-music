from django.urls import path, include

urlpatterns = [
    path("artists/", include("music.routes.artist_routes"), name="artists"),
]
