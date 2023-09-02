from django.urls import path, include

urlpatterns = [
    path("artists/", include("music.routes.artist_routes"), name="artists"),
    path("albums/", include("music.routes.album_routes"), name="albums"),
]
