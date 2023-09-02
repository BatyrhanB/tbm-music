from django.urls import path

from music.api.album_views import AlbumListAPIView, AlbumDetailAPIView

urlpatterns = [
    path("list/", AlbumListAPIView.as_view(), name="album-list"),
    path("detail/<uuid:id>/", AlbumDetailAPIView.as_view(), name="album-detail"),
]
