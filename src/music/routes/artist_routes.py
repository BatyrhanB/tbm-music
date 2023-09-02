from django.urls import path

from music.api.artist_views import ArtistAPIView, ArtistDetailAPIView


urlpatterns = [
    path("list/", ArtistAPIView.as_view(), name="artist-list"),
    path("detail/<uuid:id>/", ArtistDetailAPIView.as_view(), name="artist-detail"),
]
